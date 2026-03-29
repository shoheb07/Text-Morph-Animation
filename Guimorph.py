import tkinter as tk

class TextMorph:
    def __init__(self, root, text1, text2):
        self.root = root
        self.text1 = text1
        self.text2 = text2
        self.steps = 20
        self.current_step = 0

        self.label = tk.Label(root, text=text1, font=("Arial", 30))
        self.label.pack(pady=50)

        self.animate()

    def blend_text(self):
        result = ""
        for i in range(len(self.text1)):
            if i < self.current_step:
                result += self.text2[i] if i < len(self.text2) else ""
            else:
                result += self.text1[i]
        return result

    def animate(self):
        if self.current_step <= max(len(self.text1), len(self.text2)):
            text = self.blend_text()
            self.label.config(text=text)

            # Fade effect (color change)
            color_val = int(255 - (self.current_step * 10))
            color_val = max(0, color_val)
            color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"

            self.label.config(fg=color)

            self.current_step += 1
            self.root.after(100, self.animate)


root = tk.Tk()
root.title("Text Morph Animation")

app = TextMorph(root, "HELLO", "PYTHON")

root.mainloop()
