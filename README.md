# 🐍 Python Notes

This repository contains my personal notes on Python, organized and written in LaTeX. It's designed as a structured reference for quickly understanding Python concepts, syntax, and common use cases. Whether you're a beginner or revisiting Python, this document provides summarized explanations with examples.

## 📘 About the Project

- **Format**: PDF generated from LaTeX
- **Content**: Core Python topics with examples, syntax highlights, and summary tables
- **Purpose**: For learning, revision, and teaching purposes

## 📂 Structure

- `Python_Files/`: Contains example `.py` files referenced in the notes
- `latex/`: LaTeX source files for the Python guide
- `output/`: Compiled PDF files

## ✅ Features

- Clean, structured layout using LaTeX
- Code examples in separate files
- Covers fundamental and intermediate Python topics
- Easy to expand as new topics are added

## 🛠️ Setup Instructions (for Minted Support)

This project uses the `minted` package for syntax-highlighted code blocks in LaTeX. Follow these steps to compile successfully:

### 1. Install Python Pygments Package

Make sure you have Python installed, then run:

```bash
pip install Pygments
````

### 2. Compile with `--shell-escape`

The LaTeX file must be compiled with the `--shell-escape` flag enabled. Example:

```bash
pdflatex -synctex=1 -interaction=nonstopmode --shell-escape your_file.tex
```

If using **TeXstudio**, use this custom command:

```bash
pdflatex -synctex=1 -interaction=nonstopmode --shell-escape %.tex | txs:///view-pdf
```

> ⚠️ Without `--shell-escape`, the `minted` code blocks will not render correctly.


## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

Siddhart Patel  
Student at HTW Berlin, Lab Assistant, and Python Instructor  
[Website](https://siddharthpatelde.github.io/Portfolio/index.html) • [Email](siddharthpatel.de@gmail.com)

---

> "Simple code. Clear logic. Powerful understanding."
