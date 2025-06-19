import os
from tkinter import Tk, filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs(file_paths, output_path):
    merger = PdfMerger()
    for pdf in file_paths:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def main():
    root = Tk()
    root.withdraw()  # GUIウィンドウを非表示にする

    messagebox.showinfo("PDFマージ", "複数のPDFファイルを選択してください（CtrlやShiftで複数選択可能）")
    file_paths = filedialog.askopenfilenames(title="PDFファイルを選択", filetypes=[("PDF files", "*.pdf")])
    
    if not file_paths:
        messagebox.showwarning("警告", "ファイルが選択されていません。")
        return

    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="保存ファイル名を指定してください"
    )

    if not output_path:
        messagebox.showwarning("警告", "保存先が指定されていません。")
        return

    try:
        merge_pdfs(file_paths, output_path)
        messagebox.showinfo("成功", f"PDFのマージが完了しました:\n{output_path}")
    except Exception as e:
        messagebox.showerror("エラー", f"エラーが発生しました:\n{str(e)}")

if __name__ == "__main__":
    main()
