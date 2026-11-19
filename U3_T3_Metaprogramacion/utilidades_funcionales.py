from functools import wraps
import time
from typing import Any, Callable, List, Tuple


def configurar_impuestos(tasa: float) -> Callable[[List[float]], List[float]]:
  """Closure que retiene 'tasa' en su memoria léxica y devuelve una función pura."""
  if tasa < 0:
    raise ValueError("La tasa de impuesto no puede ser negativa.")

  def calcular_precios_finales(precios: List[float]) -> List[float]:
    factor = 1.0 + tasa
    return [round(precio * factor, 2) for precio in precios]

  return calcular_precios_finales


def trazabilidad(funcion: Callable[..., Any]) -> Callable[..., Any]:
  """Decorador 1: intercepta argumentos, imprime log en consola y ejecuta la función."""

  @wraps(funcion)
  def wrapper(*args: Any, **kwargs: Any) -> Any:
    print(f"[LOG - TRAZABILIDAD] Ejecutando '{funcion.__name__}'")
    print(f"  -> Argumentos recibidos: {args}")
    if kwargs:
      print(f"  -> Argumentos clave: {kwargs}")
    return funcion(*args, **kwargs)

  return wrapper


def medir_rendimiento(
    funcion: Callable[..., Any],
) -> Callable[..., Tuple[Any, float]]:
  """Decorador 2: mide tiempo antes y después y devuelve (resultado, tiempo_ejecucion)."""

  @wraps(funcion)
  def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, float]:
    inicio = time.perf_counter()
    resultado = funcion(*args, **kwargs)
    fin = time.perf_counter()
    tiempo_ejecucion = fin - inicio
    return resultado, tiempo_ejecucion

  return wrapper