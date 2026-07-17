# ==============================================
# FASE 5 - EVALUACIÓN FINAL POA
# Daniela Bastidas
# Gestión de precios y promociones
# ==============================================

CATEGORIA_DESCUENTO = "Platos Principales"
UMBRAL_PRECIO = 20000
PORCENTAJE_DESCUENTO = 0.15

menu_restaurante = [
    ["Sopa de verduras", "Entradas", 12000],
    ["Filete de res a la parrilla", "Platos Principales", 28500],
    ["Arroz con pollo", "Platos Principales", 18900],
    ["Pasta carbonara", "Platos Principales", 22000],
    ["Ensalada mixta", "Entradas", 9500],
    ["Helado de vainilla", "Postres", 8200],
    ["Costillas de cerdo BBQ", "Platos Principales", 32000]
]

def calcular_precio_final(categoria, precio_base):
    descuento = 0
    if categoria == CATEGORIA_DESCUENTO and precio_base > UMBRAL_PRECIO:
        descuento = precio_base * PORCENTAJE_DESCUENTO
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base
    return precio_final, descuento

print("="*80)
print(f"{'MENÚ CON PROMOCIÓN':^80}")
print("="*80)
print(f"Promoción: 15% | Categoría: {CATEGORIA_DESCUENTO} | Mayor a ${UMBRAL_PRECIO:,}")
print("-"*80)
print(f"{'Producto':<30} {'Categoría':<20} {'Precio Base':>12} {'Descuento':>12} {'Precio Final':>14}")
print("-"*80)

for item in menu_restaurante:
    nombre, cat, precio = item
    final, desc = calcular_precio_final(cat, precio)
    print(f"{nombre:<30} {cat:<20} ${precio:>11,} ${desc:>11,.0f} ${final:>13,.0f}")

print("="*80)
