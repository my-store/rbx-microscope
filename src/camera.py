from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import Frame, Label, Button
from time import strftime, sleep
from os.path import join, exists
from datetime import datetime
from threading import Thread
from os import makedirs
import cv2


class RbxCamera(Frame):
    master: Frame
    header_frame: Frame
    option_frame: Frame
    camera: Label
    camera_label: str
    camera_source: int
    video_frame: cv2.VideoCapture|None
    video_recorder: cv2.VideoWriter
    flip: int|None = None
    width: int
    height: int
    background: str
    header_background: str
    header_color: str
    preload: bool
    capturing: bool
    font_path: str
    snapshot_path: str
    snapshot_name: str
    recorded_path: str
    recorded_name: str


    def __init__(self,
                 master: Frame,
                 camera_source: int,
                 camera_label: str,
                 width: int,
                 height: int,
                 background: str,
                 header_background: str,
                 header_color: str,
                 snapshot_name: str,
                 recorded_name: str,
                 flip=None) -> None:

        super().__init__(master)

        self.master = master

        self.video_frame = None

        self.width = width
        self.height = height

        self.camera_source = camera_source

        self.flip = flip

        self.preload = True
        self.capturing = False

        self.background = background
        self.header_background = header_background
        self.header_color = header_color

        self.font_path = 'assets/fonts'

        self.snapshot_path = 'assets/img/snapshot'
        self.snapshot_name = snapshot_name

        self.recorded_path = 'assets/video/recorded'
        self.recorded_name = recorded_name

        self.camera_label = camera_label

        self.camera = Label(self, borderwidth=0)
        self.camera.pack(fill='x', side='bottom')

        self.display_header_options()

        self.display_tmp_video()


    def load_font(self, font: str, size: int):
        font_path = join(self.font_path, *font.split('/'))
        font = ImageFont.truetype(font_path, size)
        return font
    

    def insert_text(self, image: Image.new, text: str, size: int=10, font: str|None=None, x: int=0, y: int=0):
        if x == 0:
            x = (self.width / 2) - (5*len(text))
        if y == 0:
            y = (self.height / 2) - 25
        if font:
            font = self.load_font(font, size)
        else:
            font = self.load_font('subwich/Subwich.otf', size)
        drawer = ImageDraw.Draw(image)
        drawer.text(xy=(x, y), text=text, font=font)


    def toggle_flip(self, direction: str):
        if not self.video_frame:
            return

        self.master.winfo_toplevel().update_idletasks()

        current_state: int|None = self.flip

        # Flipped
        if current_state:
            self.flip = None
        # Not flipped
        else:
            if direction == 'vertical':
                self.flip = -1
            if direction == 'horizontal':
                self.flip = 1


    def display_header_options(self):
        self.header_frame = Frame(self, bg=self.header_background)
        self.header_frame.pack(fill='x', expand=True)

        label = Label(self.header_frame,
                      text=self.camera_label,
                      anchor='w',
                      borderwidth=0,
                      bg=self.header_background,
                      foreground=self.header_color,
                      font=('', 9, 'bold'))
        label.pack(side='left', padx=(10, 0), fill='x', expand=True)

        self.option_frame = Frame(self.header_frame, bg=self.header_background)
        self.option_frame.pack(side='right', padx=(0, 10))

        flip_hor = Button(self.option_frame,
                     borderwidth=0,
                     background=self.header_background,
                     activebackground=self.header_background,
                     activeforeground=self.background,
                     foreground=self.header_color,
                     text='FH',
                     cursor='hand2',
                     command=lambda: self.toggle_flip('horizontal'))
        flip_hor.grid(row=0, column=0)

        flip_ver = Button(self.option_frame,
                     borderwidth=0,
                     background=self.header_background,
                     activebackground=self.header_background,
                     activeforeground=self.background,
                     foreground=self.header_color,
                     text='FV',
                     cursor='hand2',
                     command=lambda: self.toggle_flip('vertical'))
        flip_ver.grid(row=0, column=1)

        cap = Button(self.option_frame,
                     borderwidth=0,
                     background=self.header_background,
                     activebackground=self.header_background,
                     activeforeground=self.background,
                     foreground=self.header_color,
                     text='CAP',
                     cursor='hand2',
                     command=self.snapshot)
        cap.grid(row=0, column=2)

        self.switch_button = Button(self.option_frame,
                     borderwidth=0,
                     background='#ad152e',
                     activebackground='#ad152e',
                     activeforeground=self.background,
                     foreground=self.header_color,
                     text='Off',
                     cursor='hand2',
                     command=lambda: self.turn_off() if self.video_frame else self.turn_on())
        self.switch_button.grid(row=0, column=3)


    def display_tmp_video(self):
        tmp_image = Image.new(mode='RGB', color=self.background, size=(self.width, self.height))

        # Camera status text
        st = 'Loading' if self.preload else 'Off'
        self.insert_text(image=tmp_image, text=st, size=17)

        tmp_image = ImageTk.PhotoImage(image=tmp_image)

        if not self.preload:
            self.camera.image = ''
            self.camera.configure(image='')

        self.camera.image = tmp_image
        self.camera.configure(image=tmp_image)

    def turn_off(self):
        self.master.winfo_toplevel().update_idletasks()
        self.master.winfo_toplevel().after_cancel(self.update_image)
        self.switch_button.configure(text='Off', background='#ad152e', activebackground='#ad152e')

        self.preload = False
        self.display_tmp_video()

        if self.video_frame and self.video_frame.isOpened():
            Thread(target=self.video_frame.release).start()
            self.video_frame = None

    def turn_on(self):
        self.preload = True
        self.display_tmp_video()
        self.switch_button.configure(text='On', background='#15ad27', activebackground='#15ad27')
        Thread(target=self.run).start()


    def snapshot(self):
        if not self.video_frame or self.capturing:
            return

        self.capturing = True

        def snap():
            status, frame = self.get_frame()
            if status:

                if not exists(self.snapshot_path):
                    makedirs(self.snapshot_path)

                fname = f'{self.snapshot_name}-{strftime("%d-%m-%Y-%H-%M-%S")}.jpg'
                fpath = join(self.snapshot_path, fname)

                img = Image.fromarray(frame)
                w, h = img.size
                w *= 2
                h *= 2
                img = img.resize((w, h), Image.LANCZOS)

                date = datetime.now()
                hour = str(date.hour)
                minute = str(date.minute)
                hour = '0' + hour if len(hour) < 2 else hour
                minute = '0' + minute if len(minute) < 2 else minute
                timestamp = f'{hour}:{minute} WIB'
                font = 'bebas-neue/BebasNeue-Regular.otf'
                self.insert_text(image=img, text='RBX Digital Microscope', size=27, x=20, y=h-68, font=font)
                self.insert_text(image=img, text=timestamp, size=22, x=20, y=h-38, font=font)

                img.save(fpath)
                img.close()

                sleep(0.5)

                self.capturing = False

        Thread(target=snap).start()


    def get_frame(self) -> tuple[bool, cv2.typing.MatLike|None]:
        self.master.winfo_toplevel().update_idletasks()

        if self.video_frame:
            _, frame = self.video_frame.read()
            if _:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if self.flip:
                    frame = cv2.flip(frame, self.flip)
                return (True, frame)

        return (False, None)


    def run(self):
        try:
            self.master.winfo_toplevel().update_idletasks()
            self.video_frame = cv2.VideoCapture(self.camera_source)
            # if not self.video_frame.isOpened():
            #     raise ValueError("Unable to open video source", self.camera_source)
            self.update_image()
        except:
            self.turn_off()


    def update_image(self) -> None:
        status, frame = self.get_frame()

        if status:
            resized_frame = cv2.resize(frame, (self.width, self.height))
            imaged_frame = Image.fromarray(resized_frame)

            if self.capturing:
                self.insert_text(image=imaged_frame, text='SHOOTED', size=30)

            photo_image = ImageTk.PhotoImage(image=imaged_frame)

            self.camera.image = photo_image
            self.camera.configure(image=photo_image)

            self.camera.after(15, self.update_image)


    def __del__(self) -> None:
        try:
            if self.video_frame.isOpened():
                self.video_frame.release()
            cv2.destroyAllWindows()
        except:
            pass