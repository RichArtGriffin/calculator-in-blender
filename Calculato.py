import bpy

variable_a = ""
variable_b = ""
arithmetic_operation = ""
Resultado = "" + variable_a


"""def calculate_result(value_a, value_b, calculate_operator):
    result_operator = ""
    if calculate_operator == "+":
        result_operator = value_a + value_b
        print("sumando")
    elif calculate_operator == "-":
        result_operator = value_a - value_b
        print("restando")
    elif calculate_operator == "*":
        result_operator = value_a * value_b
        print("multiplicando")
    elif calculate_operator == "/":
        result_operator = value_a / value_b
        print("Dividiendo")
    return result_operator"""

# Operadores aritmeticos escritos
class SumaOperator(bpy.types.Operator):
    bl_idname = "object.suma"
    bl_label = "Botón Suma"

    def execute(self, context):
        print("¡Botón 1 presionado!")
        return {'FINISHED'}

class RestaOperator(bpy.types.Operator):
    bl_idname = "object.resta"
    bl_label = "Botón Resta"

    def execute(self, context):
        print("¡Botón 1 presionado!")
        return {'FINISHED'}

class MultiplicationOperator(bpy.types.Operator):
    bl_idname = "object.multiplication"
    bl_label = "Botón Multiplication"

    def execute(self, context):
        print("¡Botón 1 presionado!")
        return {'FINISHED'}

class DivisionOperator(bpy.types.Operator):
    bl_idname = "object.division"
    bl_label = "Botón Division"

    def execute(self, context):
        print("¡Botón 1 presionado!")
        return {'FINISHED'}

# Operadores numericos escritos_________________________________________
class NumberOneOperator(bpy.types.Operator):
    bl_idname = "object.simple1"
    bl_label = "Botón Number One"

    def execute(self, context):
        global variable_a
        variable_a = variable_a +"1"
        print("1")
        return {'FINISHED'}

class NumberTwoOperator(bpy.types.Operator):
    bl_idname = "object.simple2"
    bl_label = "Botón Number Two"

    def execute(self, context):
        global variable_a
        variable_a = variable_a +"2"
        print("2")
        return {'FINISHED'}
# interfaces
class CalculatorPanel(bpy.types.Panel):
    bl_label = "Calculadora"
    bl_idname = "TOOL_PT_calculator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Calculator"

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        row = box.row()
        split = row.split(factor=1/5)
        split.operator("object.simple1", text="=")
        split.label(text = Resultado + variable_a + arithmetic_operation + variable_b )
        
        row = layout.row(align=True)
        row.operator("object.simple1", text="7")
        row.operator("object.simple1", text="8")
        row.operator("object.simple1", text="9")
        
        row = layout.row(align=True)
        row.operator("object.simple1", text="4")
        row.operator("object.simple1", text="5")
        row.operator("object.simple1", text="6")
        
        row = layout.row(align=True)
        row.operator("object.simple1", text="1")
        row.operator("object.simple2", text="2")
        row.operator("object.simple1", text="3")
        
        row = layout.row(align=True)
        row.operator("object.suma", text="+")
        row.operator("object.resta", text="-")
        row.operator("object.multiplication", text="*")
        row.operator("object.division", text="/")


def register():
    bpy.utils.register_class(CalculatorPanel)
    bpy.utils.register_class(SumaOperator)
    bpy.utils.register_class(RestaOperator)
    bpy.utils.register_class(MultiplicationOperator)
    bpy.utils.register_class(DivisionOperator)
    bpy.utils.register_class(NumberOneOperator)
    bpy.utils.register_class(NumberTwoOperator)

def unregister():
    bpy.utils.unregister_class(CalculatorPanel)
    bpy.utils.unregister_class(SumaOperator)
    bpy.utils.unregister_class(RestaOperator)
    bpy.utils.unregister_class(MultiplicationOperator)
    bpy.utils.unregister_class(DivisionOperator)
    bpy.utils.unregister_class(NumberOneOperator)
    bpy.utils.unregister_class(NumberTwoOperator)

if __name__ == "__main__":
    register()