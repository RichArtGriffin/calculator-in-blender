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
number_list = [""]
numer_active = 0

# Escribir numero
class WriteOneOperator(bpy.types.Operator):
    bl_idname = "object.write_number"
    bl_label = "Botón Write Number"
    bl_options = {'REGISTER', 'UNDO'}
    string_property: StringProperty(name="Input String",description="Enter a string",default="",)
    def execute(self, context):
        global number_list
        global numer_active
        number_list[numer_active] = number_list[numer_active] + self.string_property
        print("press to " + self.string_property)
        return {'FINISHED'}

# Generar Operador y dos nuevos item en la lista
class NewOperator(bpy.types.Operator):
    bl_idname = "object.new_operator"
    bl_label = "Botón New Operator"
    bl_options = {'REGISTER', 'UNDO'}
    string_property: StringProperty(name="Operator String",description="Enter a string",default="",)
    def execute(self, context):
        global number_list
        global numer_active
        numer_active = numer_active + 2
        number_list.append(self.string_property)
        number_list.append("")
        return {'FINISHED'}
# Calculate result
class EqualOperator(bpy.types.Operator):
    bl_idname = "object.equal_operator"
    bl_label = "Botón Equal Operator"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        pass

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
        split.operator( "object.equal_operator", text="=")
        split.label(text = "".join(number_list) )
        
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
        row.operator("object.new_operator", text="+").string_property = "+"
        row.operator("object.new_operator", text="-").string_property = "-"
        row.operator("object.new_operator", text="*").string_property = "*"
        row.operator("object.new_operator", text="/").string_property = "/"


def register():
    bpy.utils.register_class(CalculatorPanel)
    bpy.utils.register_class(WriteOneOperator)
    bpy.utils.register_class(NewOperator)
    bpy.utils.register_class(EqualOperator)

def unregister():
    bpy.utils.unregister_class(CalculatorPanel)
    bpy.utils.unregister_class(WriteOneOperator)
    bpy.utils.unregister_class(NewOperator)
    bpy.utils.unregister_class(EqualOperator)

if __name__ == "__main__":
    register()