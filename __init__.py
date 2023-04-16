import bpy
from bpy.props import StringProperty

bl_info = {
    "name": "Calculadora",
    "author": "RichArtGriffin",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Panel de herramientas",
    "description": "Descripcion del add-on",
}

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

class WriteOneOperator(bpy.types.Operator):
    bl_idname = "object.write_number"
    bl_label = "Botón Write Number"
    bl_options = {'REGISTER', 'UNDO'}

    string_property: StringProperty(
        name="Input String",
        description="Enter a string",
        default="",
    )

    def execute(self, context):
        global variable_a
        variable_a = variable_a + self.string_property
        print("Boton" + self.string_property)
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
        split.operator("object.write_number", text="=")
        split.label(text = Resultado + variable_a + arithmetic_operation + variable_b )
        
        row = layout.row(align=True)
        row.operator("object.write_number", text="7").string_property = "7"
        row.operator("object.write_number", text="8").string_property = "8"
        row.operator("object.write_number", text="9").string_property = "9"
        
        row = layout.row(align=True)
        row.operator("object.write_number", text="4").string_property = "4"
        row.operator("object.write_number", text="5").string_property = "5"
        row.operator("object.write_number", text="6").string_property = "6"
        
        row = layout.row(align=True)
        row.operator("object.write_number", text="1").string_property = "1"
        row.operator("object.write_number", text="2").string_property = "2"
        row.operator("object.write_number", text="3").string_property = "3"
        
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
    bpy.utils.register_class(WriteOneOperator)

def unregister():
    bpy.utils.unregister_class(CalculatorPanel)
    bpy.utils.unregister_class(SumaOperator)
    bpy.utils.unregister_class(RestaOperator)
    bpy.utils.unregister_class(MultiplicationOperator)
    bpy.utils.unregister_class(DivisionOperator)
    bpy.utils.unregister_class(WriteOneOperator)

if __name__ == "__main__":
    register()