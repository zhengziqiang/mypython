from skimage import data_dir,io,color

class AVILoader:
    video_file = 'myvideo.avi'

    def __call__(self, frame):
        return video_read(self.video_file, frame)

avi_load = AVILoader()

frames = range(0, 1000, 10) # 0, 10, 20, ...
ic =io.ImageCollection(frames, load_func=avi_load)