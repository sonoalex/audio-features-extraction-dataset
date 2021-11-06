import os

class AudioLoader():
    def __init__(self, root):
        self.root = root
    def get_audio_files(self):
        audio_paths = [];
        for subdir, dirs, files in os.walk(self.root):
            for file in files:
                if not file.endswith('.wav'):
                    continue
                audio_paths.append(os.path.join(subdir, file))
        return audio_paths
