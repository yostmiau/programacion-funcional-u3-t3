from typing import Callable, Dict, List


def aplicar_funcion_orden_superior(
    transformacion: Callable[[float], float], valores: List[float]
) -> List[float]:
  """Función de orden superior: recibe una función y devuelve una nueva función."""
  nueva_funcion = lambda lista: [transformacion(x) for x in lista]
  return nueva_funcion(valores)


def calcular_resumen_empresa(
    montos: List[float], funcion_impuesto: Callable[[List[float]], List[float]]
) -> Dict[str, float | int]:
  """Calcula totales de una empresa sin mutar los datos originales."""
  montos_finales = funcion_impuesto(montos)
  return {
      "operaciones": len(montos),
      "subtotal": round(sum(montos), 2),
      "total_con_impuesto": round(sum(montos_finales), 2),
  }


def procesar_transacciones_empresas(
    transacciones: Dict[str, List[float]],
    funcion_impuesto: Callable[[List[float]], List[float]],
) -> Dict[str, Dict[str, float | int]]:
  """Procesa transacciones financieras de varias empresas de forma pura."""
  return {
      empresa: calcular_resumen_empresa(montos, funcion_impuesto)
      for empresa, montos in transacciones.items()
  }