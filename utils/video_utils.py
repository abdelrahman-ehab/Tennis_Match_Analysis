import cv2

def read_video(video_path):

    frames = []
    cap = cv2.VideoCapture(video_path)

    while True:
        ret,frame = cap.read()

        if not ret :
            break
        frames.append(frame)
    cap.release()
    return frames

def save_video(op_video_frames,op_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(op_video_path, fourcc, 24, (op_video_frames[0].shape[1], op_video_frames[0].shape[0]))
    for frame in op_video_frames:
        out.write(frame)
    out.release()