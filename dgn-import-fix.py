import rhinoscriptsyntax as rs

def safe_czech_fix(text):
    if not text: return text
    
    fixed_chars = []
    # Translate character by character to prevent Python from crashing
    for char in text:
        code = ord(char)
        
        # If the character's numeric code is in the extended range (128-255), 
        # it is a misread DGN byte. We isolate it and force it back to Czech.
        if 128 <= code <= 255:
            try:
                # Pack the raw byte and decode it using the Czech dictionary (CP1250)
                correct_char = bytes([code]).decode('cp1250')
                fixed_chars.append(correct_char)
            except:
                fixed_chars.append(char) # Fallback if something weird happens
        else:
            # Normal ASCII letters or true Unicode symbols are safely left alone
            fixed_chars.append(char)
            
    return "".join(fixed_chars)

def fix_all_czech_text_v2():
    rs.EnableRedraw(False)
    layers_fixed = 0
    text_fixed = 0
    
    # 1. Fix Layer Names
    layers = rs.LayerNames()
    if layers:
        for layer in layers:
            short_name = layer.split("::")[-1]
            new_name = safe_czech_fix(short_name)
            if short_name != new_name:
                try:
                    rs.RenameLayer(layer, new_name)
                    layers_fixed += 1
                except:
                    pass
                    
    # 2. Fix Geometry Text & Annotations
    annotations = rs.ObjectsByType(rs.filter.annotation)
    if annotations:
        for ann_id in annotations:
            old_text = rs.TextObjectText(ann_id)
            if old_text:
                new_text = safe_czech_fix(old_text)
                if old_text != new_text:
                    try:
                        rs.TextObjectText(ann_id, new_text)
                        text_fixed += 1
                    except:
                        pass

    rs.EnableRedraw(True)
    print("Encoding fix V2 complete!")
    print(f"Corrected {layers_fixed} layers and {text_fixed} text objects.")

if __name__ == "__main__":
    fix_all_czech_text_v2()
