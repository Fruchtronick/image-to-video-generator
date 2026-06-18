import gradio as gr
from moviepy.editor import ImageClip, concatenate_videoclips
from PIL import Image
import numpy as np

def image_to_video(image, duration=3, fps=24):
    # Bild in numpy Array umwandeln
    img = np.array(image)
    
    # Einfaches Video: Bild mit leichtem Zoom-Effekt
    clip = ImageClip(img).set_duration(duration)
    
    # Zoom-Effekt simulieren
    def zoom(t):
        return 1 + 0.05 * t  # Langsamer Zoom
    
    video = clip.resize(lambda t: zoom(t))
    
    output_path = "output.mp4"
    video.write_videofile(output_path, fps=fps)
    return output_path

# Gradio Interface
interface = gr.Interface(
    fn=image_to_video,
    inputs=[
        gr.Image(type="pil", label="Lade dein Bild hoch"),
        gr.Slider(1, 10, value=3, label="Videolänge in Sekunden"),
    ],
    outputs=gr.Video(label="Generiertes Video"),
    title="🖼️ Bild zu Video Generator",
    description="Lade ein Bild hoch und lass es zu einem kurzen Video werden. Perfekt für Anfänger!",
    examples=None
)

if __name__ == "__main__":
    interface.launch()