# Rhinoceros-dgn-import-czech-encoding-fix
A Python script for Rhino 7/8 that fixes scrambled Czech (Windows-1250) characters in layer names and text geometry after importing DGN files. It uses a byte-mapping dictionary to correct mojibake caused by Rhino defaulting to Western encoding during import.
