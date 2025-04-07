"""
interface_adapters/controllers/etl_controller.py
Controlador que orquesta la ejecución del proceso ETL completo sin requerir input del usuario.
"""

class ETLController:
    """
    Controlador principal que define el flujo ETL secuencial.
    """
    def __init__(self, bc_use_cases):
        self.bc_use_cases = bc_use_cases

    def run_etl_process(self):
        """
        1. Conecta a BC y lista las entidades disponibles.
        2. Imprime la lista de entidades.
        3. Obtiene la lista de clientes.
        4. Imprime los clientes y los guarda en un CSV.
        """
        # 1. Obtener entidades
        entities = self.bc_use_cases.get_entities()
        print("Entidades disponibles en la API de Business Central:")
        for entity in entities.get("value", []):
            print(f"- {entity['name']}")

        # 2. Obtener clientes
        customers = self.bc_use_cases.get_customers()
        print("\nClientes disponibles en Business Central:")
        for cust in customers.get("value", []):
            print(cust)

        # 3. Exportar clientes a CSV
        self.bc_use_cases.export_customers_to_csv(customers, file_path="customers_export.csv")
        print("\nLos clientes se han guardado en 'customers_export.csv'.")
