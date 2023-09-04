"""Extracting the chart with DePlot """

from transformers import Pix2StructProcessor, Pix2StructForConditionalGeneration
from PIL import Image
import pandas as pd

# HF will load from cache if pre downloaded
processor = Pix2StructProcessor.from_pretrained('google/deplot')
model = Pix2StructForConditionalGeneration.from_pretrained('google/deplot')

def extract_text_from_image(image: Image.Image, prompt_text: str = "Generate the underlying data table of the figure below:") -> str:
    """
    Extracts data from an image using the Pix2Struct model.
    """
    inputs = processor(images=image, text=prompt_text, return_tensors="pt")
    predictions = model.generate(**inputs, max_new_tokens=1024)
    extracted_text = processor.decode(predictions[0], skip_special_tokens=True)

    return extracted_text

def text_to_structures(text: str):
    """
    Converts text output from the model to various formats.

    This is specific to Deplot's output - so might need to be extended for further models.
    """
    # Remove special tokens like <pad> and </s>
    text = text.replace('<pad>', '').replace('</s>', '')
    
    # Split the text by the row separator
    rows = text.split('<0x0A>')
    
    # Remove any empty or None rows
    rows = [row.strip() for row in rows if row.strip()]
    
    # Extract headers and data
    headers = rows[0].split('|')
    print("Headers", headers)
    headers = [header.strip() for header in headers]
    
    data = []
    for row in rows[1:]:
        row_data = row.split('|')
        row_data = [item.strip() for item in row_data]
        data.append(row_data)

    print("Data", data)
    
    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=headers)
    
    # Create a Markdown table
    md_table = '| ' + ' | '.join(headers) + ' |\n'
    md_table += '| ' + '--- |' * len(headers) + '\n'
    for row in data:
        md_table += '| ' + ' | '.join(row) + ' |\n'
    
    # Create a LaTeX tabular table
    latex_table = '\\begin{tabular}{' + 'c' * len(headers) + '}\n'
    latex_table += ' & '.join(headers) + ' \\\\\n\\hline\n'
    for row in data:
        latex_table += ' & '.join(row) + ' \\\\\n'
    latex_table += '\\end{tabular}'

    return df, md_table, latex_table
