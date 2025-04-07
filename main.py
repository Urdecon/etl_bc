"""
main.py
Punto de entrada de la aplicación: crea instancias, inyecta dependencias
y ejecuta el proceso ETL secuencial.
"""

from infrastructure.business_central.bc_client import BCClient
from infrastructure.business_central.bc_repository import BCRepository

from domain.services.transform_service import TransformService
from application.use_cases.bc_use_cases import BCUseCases
from interface_adapters.controllers.etl_controller import ETLController

def main():
    # 1. Infraestructura
    bc_client = BCClient()
    bc_repository = BCRepository(bc_client)

    # 2. Dominio/Servicios
    transform_service = TransformService()

    # 3. Casos de uso
    bc_use_cases = BCUseCases(bc_repository, transform_service)

    # 4. Controlador
    controller = ETLController(bc_use_cases)

    # 5. Ejecutar el proceso ETL secuencial
    controller.run_etl_process()

if __name__ == "__main__":
    main()
