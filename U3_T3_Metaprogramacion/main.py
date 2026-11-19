import json
from logica_pura import aplicar_funcion_orden_superior, procesar_transacciones_empresas
from utilidades_funcionales import (
    configurar_impuestos,
    medir_rendimiento,
    trazabilidad,
)


def imprimir_json(titulo: str, datos: object) -> None:
  print(titulo)
  print(json.dumps(datos, indent=2, ensure_ascii=False))


def main() -> None:
  # --- PARTE 2 ---
  print("\n=== PARTE 2: MOTOR MATEMÁTICO Y CLOSURES ===")
  precios_base = [150.0, 320.5, 95.0]
  iva_15 = configurar_impuestos(0.15)
  precios_finales = iva_15(precios_base)
  ajuste_lambda = aplicar_funcion_orden_superior(
      lambda x: round(x * 1.10, 2), precios_base
  )

  print(f"Precios originales (intactos): {precios_base}")
  print(f"Precios con IVA 15% (closure): {precios_finales}")
  print(f"Función orden superior (+10%): {ajuste_lambda}")

  empresas = {
      "AndesCorp": [1000.0, 450.0, 250.0],
      "PacificoTrade": [2100.0, 800.0],
      "CostaLogistica": [600.0, 350.0, 190.0],
  }

  # --- PARTE 3A: Sintaxis declarativa '@' ---
  print("\n=== PARTE 3A: COMPOSICIÓN DECLARATIVA (@) ===")

  @medir_rendimiento
  @trazabilidad
  def procesar_con_arroba(datos_empresas, calc_impuesto):
    return procesar_transacciones_empresas(datos_empresas, calc_impuesto)

  resultado_arroba, tiempo_arroba = procesar_con_arroba(empresas, iva_15)
  imprimir_json("Resultado:", resultado_arroba)
  print(f"Tiempo de ejecución: {tiempo_arroba:.8f} s")

  # --- PARTE 3B: Evaluación explícita Dec2(Dec1(Funcion())) ---
  print("\n=== PARTE 3B: COMPOSICIÓN EXPLÍCITA Dec2(Dec1(Funcion())) ===")

  def procesar_nucleo(datos_empresas, calc_impuesto):
    return procesar_transacciones_empresas(datos_empresas, calc_impuesto)

  # Dec2 = medir_rendimiento | Dec1 = trazabilidad
  pipeline_manual = medir_rendimiento(trazabilidad(procesar_nucleo))
  resultado_manual, tiempo_manual = pipeline_manual(empresas, iva_15)
  imprimir_json("Resultado:", resultado_manual)
  print(f"Tiempo de ejecución: {tiempo_manual:.8f} s")


if __name__ == "__main__":
  main()