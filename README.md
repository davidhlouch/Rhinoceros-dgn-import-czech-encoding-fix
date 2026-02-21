# Rhinoceros-dgn-import-czech-encoding-fix
A Python script for Rhino 7/8 that fixes scrambled Czech (Windows-1250) characters in layer names and text geometry after importing DGN files. It uses a byte-mapping dictionary to correct mojibake caused by Rhino defaulting to Western encoding during import.

# Rhino DGN Czech Encoding Fix

When importing MicroStation DGN files into Rhinoceros 3D, Central European characters (Windows-1250 code page) are often misread as Western European (ISO-8859-1/Windows-1252). This results in scrambled text in both layer names and geometry (e.g., "č" becomes "è", "ř" becomes "ø"). 

This Python script crawls through your Rhino file and uses a brute-force dictionary to instantly translate the scrambled text back to correct Czech characters.

## ⚠️ Known Limitation: The Missing "Š"
Due to a hardcoded bug in Rhino's internal DGN parser, the uppercase **"Š"** (byte `0x8A` / decimal 138) is completely deleted during the import process. Because the data is physically destroyed before the file opens, **this script cannot restore the uppercase Š.** All other problematic characters, including lowercase "š", are successfully fixed.

The bug is reported to McNeel [here](https://discourse.mcneel.com/t/encoding-bug-on-dgn-import/216194).

## How to Use
1. Import your problematic `.dgn` file into Rhino.
2. Type **`ScriptEditor`** (Rhino 8) or **`EditPythonScript`** (Rhino 7) into the command line and press Enter.
3. Open a new Python 3 (or Python) script.
4. Copy and paste the script code into the editor.
5. Click the **Run/Play** button. 

The script will automatically scan all layer names and text/annotation objects, replace the corrupted characters, and print a summary of how many items were fixed.
