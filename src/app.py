# SOURCE CODE - MICROSCOPE TRIPLE CAMERA V1.0
# Creator: Izzat Alharis | RBX FAMILY BREBES
# Created at: Jan 09 2024


from tkinter import Tk, Frame
from camera import RbxCamera
import sys


app = Tk()
app.title('RBX Digital Microscope')
app.resizable(False, False)

main_frame = Frame(app)
main_frame.pack(fill='both', expand=True)

microscope_flip = None
microscope = RbxCamera(master=main_frame,
              camera_source=0,
              camera_label='HD CAMERA 1600x',
              width=700,
              height=522,
              flip=microscope_flip,
              background='#377cad',
              header_background='#265475',
              header_color='#eee',
              snapshot_name='Microscope-image',
              recorded_name='Microscope-video')
microscope.grid(row=0, column=0)

left_frame = Frame(main_frame)
left_frame.grid(row=0, column=1, sticky='n')

digital_1_flip = -1
digital_1 = RbxCamera(master=left_frame,
                     camera_source=1,
                     camera_label='DIGITAL 1',
                     width=350,
                     height=250,
                     flip=digital_1_flip,
                     background='#37a2ad',
                     header_background='#23676e',
                     header_color='#eee',
                     snapshot_name='Digital1-image',
                     recorded_name='Digital1-video')
digital_1.grid(row=0, column=0)

digital_2_flip = None
digital_2 = RbxCamera(master=left_frame,
                     camera_source=2,
                     camera_label='DIGITAL 2',
                     width=350,
                     height=250,
                     flip=digital_2_flip,
                     background='#37a2ad',
                     header_background='#23676e',
                     header_color='#eee',
                     snapshot_name='Digital2-image',
                     recorded_name='Digital2-video')
digital_2.grid(row=1, column=0)


def standby():
    microscope.turn_off()
    digital_1.turn_off()
    digital_2.turn_off()


def close_app():
    app.quit()
    sys.exit()


if __name__ == '__main__':
    app.after(1000, standby)
    app.protocol("WM_DELETE_WINDOW", close_app)
    app.mainloop()
