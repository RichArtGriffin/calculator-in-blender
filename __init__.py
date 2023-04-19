import bpy
from bpy.props import StringProperty
import bpy.utils.previews
import os

bl_info = {
    "name": "Calculadora",
    "author": "RichArtGriffin",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Panel de herramientas",
    "description": "Descripcion del add-on",
}
number_list = [""]
number_active = 0
last_result = 0
last_operation = ""

# Variable global para almacenar tus iconos
custom_icons = None

def load_custom_icons():
    global custom_icons
    custom_icons = bpy.utils.previews.new()

    # Carga los iconos desde el directorio de recursos de tu add-on
    icons_dir = bpy.path.abspath("//resources")

    # Registra los iconos
    custom_icons.load("logo_calculator", os.path.join(icons_dir, "Logo_Calculator.png"), 'IMAGE')

def unload_custom_icons():
    global custom_icons
    bpy.utils.previews.remove(custom_icons)

# Escribir numero
class WriteOneOperator(bpy.types.Operator):
    bl_idname = "object.write_number"
    bl_label = "Botón Write Number"
    bl_options = {'REGISTER', 'UNDO'}
    string_property: StringProperty(name="Input String",description="Enter a string",default="",)
    def execute(self, context):
        global number_list
        global number_active
        global last_result
        number_list[number_active] = number_list[number_active] + self.string_property
        last_result = number_list[0]
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
        global number_active
        global last_operation
        if number_list[-1] == "":
            number_list[-2] = str(self.string_property)
        else:
            number_active = number_active + 2
            number_list.append(self.string_property)
            number_list.append("")
        return {'FINISHED'}


# Calculate result
class EqualOperator(bpy.types.Operator):
    bl_idname = "object.equal_operator"
    bl_label = "Botón Equal Operator"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        global number_list
        global number_active
        global last_result
        number_active = number_active
        ref_indice = 0
        if number_active == 0:
            print("igual al mismo numero")
            return {'FINISHED'}
        if number_active == 2 and number_list[-1] == "":
            number_list = number_list[:-2]
            return {'FINISHED'}
        else:
            continuar = True
            for indice in number_list:
                ref_indice = ref_indice + 1
                print(str(indice))
                #if number_list[-2] == "+" or number_list[-2] == "-" or number_list[-2] == "*" or number_list[-2] == "/" and number_list[-1] == "" :
                #    number_list = number_list[:-2]
                #    return {'FINISHED'}
                if indice == "+" and continuar:
                    last_result = float(last_result) + float(number_list[int(ref_indice)])
                    print("suma :" + str(last_result))
                        
                elif indice == "-"and continuar:
                    last_result = float(last_result) - float(number_list[int(ref_indice)])
                    print("Resta :" + str(last_result))
                    
                elif indice == "*"and continuar:
                    last_result = float(last_result) * float(number_list[int(ref_indice)])
                    print("multiplicacion")
                    
                elif indice == "/"and continuar:
                    last_result = float(last_result) / float(number_list[int(ref_indice)])
                    print("division")
                    
            print("numero activo :" + str(last_result))
        number_list.clear()
        number_list.append(str(int(last_result)))
        number_active = 0
        return {'FINISHED'}
# Clear Operations
class ClearOperator(bpy.types.Operator):
    bl_idname = "object.clear"
    bl_label = "Botón Clear"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        global number_active
        number_list.clear()
        number_list.append("")
        number_active = 0
        return {'FINISHED'}

# Clear last number Operations
class ClearLasNumberOperator(bpy.types.Operator):
    bl_idname = "object.clear_last_number"
    bl_label = "Botón Clear Last Number"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        global number_list
        global number_active
        if number_active == 0 and number_list[0] == "":
            print("igual al mismo numero")
            return {'FINISHED'}
        elif number_active == 0 and number_list[0] != "":
            ref_i = str(number_list[-1])
            if len(ref_i) > 0:
                ref_i = ref_i[:-1]
                number_list[-1] = ref_i
        elif number_list[-2] == "+" or number_list[-2] == "-" or number_list[-2] == "*" or number_list[-2] == "/" and number_list[-1] == "" :
            number_list = number_list[:-2]
            ref_longitud = len(number_list) - 1
            number_active = ref_longitud
            return {'FINISHED'}
        else:
            ref_i = str(number_list[-1])
            if len(ref_i) > 0:
                ref_i = ref_i[:-1]
                number_list[-1] = ref_i
            ref_longitud = len(number_list) - 1
            number_active = ref_longitud
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
        split = row.split(factor=5/6)
        split.label(text = "".join(number_list) )
        split.operator( "object.clear_last_number", text="", icon_value=custom_icons["logo_calculator"].icon_id)

        row = layout.row(align=True)
        split = row.split(factor=1/4)
        split.operator("object.write_number", text="7").string_property = "7"
        split.operator("object.write_number", text="8").string_property = "8"
        split.operator("object.write_number", text="9").string_property = "9"
        split.operator("object.new_operator", text="+").string_property = "+"
        
        row = layout.row(align=True)
        split = row.split(factor=1/4)
        split.operator("object.write_number", text="4").string_property = "4"
        split.operator("object.write_number", text="5").string_property = "5"
        split.operator("object.write_number", text="6").string_property = "6"
        split.operator("object.new_operator", text="-").string_property = "-"
        
        row = layout.row(align=True)
        split = row.split(factor=1/4)
        split.operator("object.write_number", text="1").string_property = "1"
        split.operator("object.write_number", text="2").string_property = "2"
        split.operator("object.write_number", text="3").string_property = "3"
        split.operator("object.new_operator", text="*").string_property = "*"

        row = layout.row(align=True)
        split = row.split(factor=1/4)
        #split.operator( "object.clear", text="", icon='TRASH')
        split.operator( "object.write_number", text=".").string_property = ".   "
        split.operator( "object.write_number", text="0").string_property = "0"
        split.operator( "object.equal_operator", text="=")
        split.operator("object.new_operator", text="/").string_property = "/"
        


def register():
    bpy.utils.register_class(CalculatorPanel)
    bpy.utils.register_class(WriteOneOperator)
    bpy.utils.register_class(NewOperator)
    bpy.utils.register_class(EqualOperator)
    bpy.utils.register_class(ClearOperator)
    bpy.utils.register_class(ClearLasNumberOperator)
    load_custom_icons()

def unregister():
    bpy.utils.unregister_class(CalculatorPanel)
    bpy.utils.unregister_class(WriteOneOperator)
    bpy.utils.unregister_class(NewOperator)
    bpy.utils.unregister_class(EqualOperator)
    bpy.utils.unregister_class(ClearOperator)
    bpy.utils.unregister_class(ClearLasNumberOperator)
    unload_custom_icons()

if __name__ == "__main__":
    register()