import os
import configparser

CONFIG_FILE = "PresetCreator.ini"
PRESETS_DIR = "Presets"

def get_default_config():
    """Returns the default ini configuration if none exists."""
    return """[Presets]
Core_Baseline = NRE_Compact.md, Lightful_Ontology_Compact.md, HRE_Compact.md, Decision_Path_Compact.md
Software_Engineering_Review = NRE_Compact.md, Lightful_Ontology_Compact.md, HRE_Compact.md, Decision_Path_Compact.md, Sibling_Oriented_Architecture_AddOn.md, Semantic_Superconductivity_AddOn.md, Accessibility_Geometry_AddOn.md
Conflict_Resolution_Triage = NRE_Compact.md, Lightful_Ontology_Compact.md, HRE_Compact.md, Decision_Path_Compact.md, Conflict_Triage_AddOn.md, Alien_Ontology_AddOn.md, Epistemic_Centrifuge_AddOn.md
Full_Governance_Audit = NRE_Compact.md, Lightful_Ontology_Compact.md, HRE_Compact.md, Decision_Path_Compact.md, NRE_Governance.md, Lightful_Ontology_Governance.md, HRE_Governance.md, Decision_Path_Governance.md, Validator_Calibration_AddOn.md
Academic_Research = NRE_Compact.md, Lightful_Ontology_Compact.md, HRE_Compact.md, Decision_Path_Compact.md, Academic_Bridge_AddOn.md, Formal_Verification_AddOn.md, Graph_Inscription_AddOn.md
Creative_Writing_Editing = NRE_Compact.md, Lightful_Ontology_Compact.md, HRE_Compact.md, Decision_Path_Compact.md, Semantic_Superconductivity_AddOn.md, Adaptive_Interface_AddOn.md, Waveform_Diagnostics_AddOn.md
"""

def find_file(filename, root_path="."):
    """Recursively searches for a file, ignoring the Presets output directory."""
    for dirpath, _, files in os.walk(root_path):
        # Prevent the script from looking inside the output folder itself
        if PRESETS_DIR in os.path.split(dirpath):
            continue
        if filename in files:
            return os.path.join(dirpath, filename)
    return None

def load_or_create_config():
    """Loads the INI file, generating it first if missing."""
    if not os.path.exists(CONFIG_FILE):
        print(f"Configuration file not found. Generating default {CONFIG_FILE}...")
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            f.write(get_default_config())

    config = configparser.ConfigParser()
    # optionxform = str prevents configparser from forcing keys to lowercase
    config.optionxform = str 
    config.read(CONFIG_FILE, encoding='utf-8')
    return config

def main():
    print(f"Initializing Lightful Preset Creator...\n")
    config = load_or_create_config()

    if not os.path.exists(PRESETS_DIR):
        os.makedirs(PRESETS_DIR)
        print(f"Created output directory: {PRESETS_DIR}/")

    if 'Presets' not in config:
        print("Error: No [Presets] section found in the INI file.")
        return

    # Process each preset
    for preset_name, file_list_str in config['Presets'].items():
        files_to_include = [f.strip() for f in file_list_str.split(',') if f.strip()]
        output_filepath = os.path.join(PRESETS_DIR, f"{preset_name}.md")
        
        missing_files = []
        concatenated_content = f"# PRESET SCRIPT: {preset_name}\n"
        concatenated_content += f"> Assembled from: {', '.join(files_to_include)}\n\n"

        for filename in files_to_include:
            file_path = find_file(filename)
            
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # Inject a clear markdown break so the LLM understands file boundaries
                    concatenated_content += f"\n\n---\n## INJECTED COMPONENT: {filename}\n---\n\n"
                    concatenated_content += infile.read()
            else:
                missing_files.append(filename)
                concatenated_content += f"\n\n---\n## INJECTED COMPONENT: {filename} [ERROR: FILE NOT FOUND]\n---\n\n"

        # Write the final bundled preset
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(concatenated_content)
        
        # Terminal Feedback
        success_count = len(files_to_include) - len(missing_files)
        print(f"✅ Created: {preset_name}.md ({success_count}/{len(files_to_include)} modules injected)")
        if missing_files:
            print(f"   ⚠️  Warning - Missing files: {', '.join(missing_files)}")

    print(f"\nAll presets successfully crystallized in the '/{PRESETS_DIR}' folder.")

if __name__ == "__main__":
    main()