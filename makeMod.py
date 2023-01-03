import pathlib
import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import num2words


version = "0.1.0"


maxNum = 100

names = {}
for i in range(1, maxNum):
  names[i] = num2words.num2words(i)


infoJson = """{
  "name": "inftorio",
  "version": """ + '"' + version + '"' + """,
  "title": "Inftorio",
  "author": "TessaCoil",
  "factorio_version": "1.1",
  "dependencies": ["base >= 1.1", "Warehousing >= 0.5.7"],
  "description": "This mod adds infinite crafting recipes"
}"""


dataLua = """--data.lua

require("prototypes.recipe")
require("prototypes.item.item")
"""


locale = """
[entity-name]
number-one=One

[item-name]
"""

def caps(s):
  if ord(s[0]) <= ord('z') and ord(s[0]) >= ord('a'):
    return chr(ord(s[0])-ord('a')+ord('A')) + s[1:]
  else:
    return s

for i in range(2, maxNum):
  locale += "number-" + names[i] + "=" + caps(names[i]) + "\n"

locale += '[item-description]\n'

for i in range(2, maxNum):
  locale += "number-" + names[i] + "=The number " + str(i) + "\n"
  


allRecipes = """data:extend(
{
  {
    type = "recipe",
    name = "one",
    enabled = true,
    ingredients =
    {
    },
    result = "number-one"
  },
  {
    type = "recipe",
    name = "spicybean",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "assembling-machine-3"
  },
  {
    type = "recipe",
    name = "spicybeanaaaaa",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "express-transport-belt"
  },
  {
    type = "recipe",
    name = "spicybeanf",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "fast-inserter"
  },
  {
    type = "recipe",
    name = "spicybeanffafa",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "factory-3"
  },
  {
    type = "recipe",
    name = "spicybeanfaaaaaaaa",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "factory-2"
  },
  {
    type = "recipe",
    name = "make-personal-roboportff",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "personal-roboport-mk2-equipment"
  },
  {
    type = "recipe",
    name = "make-portable-fusion-reactorff",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "fusion-reactor-equipment"
  },
  {
    type = "recipe",
    name = "make-construction-robotff",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "construction-robot"
  },
  {
    type = "recipe",
    name = "make-warehouse",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "warehouse-basic"
  },
  {
    type = "recipe",
    name = "make-express-underground-hh",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "express-underground-belt"
  },
  {
    type = "recipe",
    name = "make-power-armor",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "power-armor-mk2"
  },
  {
    type = "recipe",
    name = "make-factory-1",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "factory-1"
  },
  {
    type = "recipe",
    name = "make-substation",
    enabled = true,
    energy_required = 0.01,
    ingredients =
    {
      {"number-one", 1},
    },
    result = "substation"
  },"""




for i in range(2, maxNum):
  name = names[i]
  allRecipes += """
  {
    type = "recipe",
    name = """ '"recipe' + str(i) + '"' + """,
    enabled = true,
    hide_from_player_crafting = true,
    ingredients =
    {
      {"number-""" + names[i-1] + """", 2},
    },
    result = "number-""" + names[i] + """"
  },"""

recipesLua = allRecipes + """
}
)"""


prototypesItemLua = """data:extend({
  {
    type = "solar-panel",
    name = "number-one",
    icon = "__inftorio__/graphics/icons/number-one.png",
    icon_size = 32,
    icon_mipmaps = 4,
    flags = {"placeable-neutral", "player-creation"},
    minable = {hardness = 0.2, mining_time = 0.5, result = "number-one"},
    max_health = 100,
    corpse = "medium-remnants",
    collision_box = {{-0.5, -0.5}, {0.5, 0.5}},
    selection_box = {{-1.0, -1.0}, {1.0, 1.0}},
    energy_source =
    {
      type = "void",
      usage_priority = "primary-output"
    },
    picture =
    {
      filename = "__inftorio__/graphics/icons/number-one.png",
      priority = "high",
      width = 32,
      height = 32
    },
    production = "26000.67kW",
  },"""
  
for i in range(1, maxNum):
  prototypesItemLua += """
  {
    type = "item",
    name = "number-""" + names[i] + """",
    icon = "__inftorio__/graphics/icons/number-""" + names[i] + """.png",
   	order = "a-a-a",
    stack_size = 500,
    icon_size = 32,"""
  if i == 1:
    prototypesItemLua += """
    place_result = "number-""" + names[i] + """","""
  prototypesItemLua += """
  },"""
  
prototypesItemLua += """
})"""




# 

itemLua = """--item.lua

local fireArmor = table.deepcopy(data.raw["armor"]["heavy-armor"]) -- copy the table that defines the heavy armor item into the fireArmor variable

fireArmor.name = "fire-armor"
fireArmor.icons = {
  {
    icon = fireArmor.icon,
    tint = {r=1,g=0,b=0,a=0.3}
  },
}

fireArmor.resistances = {
  {
    type = "physical",
    decrease = 6,
    percent = 10
  },
  {
    type = "explosion",
    decrease = 10,
    percent = 30
  },
  {
    type = "acid",
    decrease = 5,
    percent = 30
  },
  {
    type = "fire",
    decrease = 0,
    percent = 100
  }
}

local recipe = table.deepcopy(data.raw["recipe"]["heavy-armor"])
recipe.enabled = true
recipe.name = "fire-armor"
recipe.ingredients = {{"copper-plate",200},{"steel-plate",50}}
recipe.result = "fire-armor"

data:extend{fireArmor,recipe}
"""





allObjects = []

allRecipes = []



def makeNumberIcon(width, height, number, path):
  image = Image.new("RGBA", (width,height), (255,255,255,0))
  draw = ImageDraw.Draw(image)
  font = ImageFont.truetype("consola.ttf", 25)

  w, h = draw.textsize(str(number), font=font)
  draw.text((width//2-w//2, height//2-h//2-1), str(number), (255,255,255), font=font)
  image.save(path)


if __name__ == "__main__":
  modName = 'inftorio'
  if os.path.exists(modName):
    shutil.rmtree(modName)
  p = pathlib.Path(modName)
  p.mkdir(parents=True, exist_ok=True)
  
  modBaseFolder = modName + "/" + modName
  p = pathlib.Path(modBaseFolder)
  p.mkdir(parents=True, exist_ok=True)
  
  f = open(modBaseFolder + "/info.json", 'w')
  f.write(infoJson)
  f.close()
  
  f = open(modBaseFolder + "/data.lua", 'w')
  f.write(dataLua)
  f.close()
  
  p = pathlib.Path(modBaseFolder + "/locale/en")
  p.mkdir(parents=True, exist_ok=True)
  f = open(modBaseFolder + "/locale/en/names.cfg", "w")
  f.write(locale)
  f.close()
  
  prototypesFolder = modBaseFolder + "/prototypes"
  p = pathlib.Path(prototypesFolder)
  p.mkdir(parents=True, exist_ok=True)
  
  f = open(prototypesFolder + "/recipe.lua", "w")
  f.write(recipesLua)
  f.close()
  
  #f = open(modBaseFolder + "/item.lua", 'w')
  #f.write(itemLua)
  #f.close()
  
  
  prototypesItemFolder = prototypesFolder + "/item"
  p = pathlib.Path(prototypesItemFolder)
  p.mkdir(parents=True, exist_ok=True)
  
  f = open(prototypesItemFolder + "/item.lua", "w")
  f.write(prototypesItemLua)
  f.close()
  
  graphicsFolder = modBaseFolder + "/graphics"
  p = pathlib.Path(graphicsFolder)
  p.mkdir(parents=True, exist_ok=True)
  
  iconsFolder = graphicsFolder + "/icons"
  p = pathlib.Path(iconsFolder)
  p.mkdir(parents=True, exist_ok=True)
  
  for i in range(1, maxNum):
    makeNumberIcon(32, 32, i, iconsFolder + "/number-" + names[i] + ".png")
  
  
  zipName = modName + "_" + version
  if os.path.exists(zipName + ".zip"):
    os.remove(zipName + ".zip")
  shutil.make_archive(zipName, 'zip', modName)
  
  shutil.copyfile(zipName + ".zip", "C:/Users/yams/AppData/Roaming/Factorio/mods/" + zipName + ".zip")
  