import os

# Ruta base del proyecto
base_path = r"C:\Users\EfrainMejiasC\Documents\GitHub\Python_Practice\Python_Practice_Web\Python_Practice_WebApi.Solution"

# Estructura de carpetas y descripciones para los README.md
folders_with_descriptions = {
    "app": "Esta carpeta contiene toda la lógica principal de la aplicación.",
    "app/api": "Esta carpeta contiene los controladores o rutas de la API.",
    "app/api/v1": "Aquí se encuentran las rutas de la API para la versión 1.",
    "app/core": "Esta carpeta contiene configuraciones esenciales y la lógica central.",
    "app/models": "Aquí se definen los modelos que representan las entidades de la base de datos.",
    "app/schemas": "Esta carpeta contiene los esquemas Pydantic para validación de datos.",
    "app/services": "En esta carpeta se implementan los servicios y la lógica de negocio.",
    "app/tests": "Aquí se almacenan los casos de prueba para la aplicación.",
    "app/migrations": "Esta carpeta contiene los archivos de migraciones para la base de datos."
}

def create_folders_and_readmes(base_path, folders_with_descriptions):
    for folder, description in folders_with_descriptions.items():
        folder_path = os.path.join(base_path, folder)
        try:
            # Crear carpeta
            os.makedirs(folder_path, exist_ok=True)
            print(f"Carpeta creada: {folder_path}")

            # Crear README.md con descripción
            readme_path = os.path.join(folder_path, "README.md")
            with open(readme_path, "w", encoding="utf-8") as readme_file:
                readme_file.write(description)
            print(f"Archivo README.md creado en: {readme_path}")
        except Exception as e:
            print(f"Error al crear la carpeta o el archivo README.md en {folder_path}: {e}")

if __name__ == "__main__":
    create_folders_and_readmes(base_path, folders_with_descriptions)

