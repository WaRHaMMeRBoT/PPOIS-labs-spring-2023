# PPOIS 1 lab

## Первая лабораторная 4 семестра по ППОИС.

![image](https://user-images.githubusercontent.com/91974808/218490773-855b7f65-c9ed-46d1-973b-2fca9c544ff3.png)

#### Модель животного мира - 2

Предметная область: взаимодействие жителей леса (равнины, океана, и пр), в формате игровой симуляции

Важные сущности: животное, передвижение, еда, питание, размножение, умирание, старость, голод, хищники, травоядные,
растения, местопребывание (клетка на поле)

Моделировать в виде пошаговой симуляции, с возможностью добавления животных или растений на клетку поля


# Quick start
````
git clone https://github.com/Deniskoltovich/PPOIS-3-sem.git
cd PPOIS-3-sem/
````

````
python3 lab1/main.py <command>
````
Available commands:
```
  --nextday                     Imitate new day and changes garden's state
  
  --desinfect <field_number>    Kill all pests and illnesses on the field
  
  --heal <field_number>         Increases plant's health 
  
  --hydrate <field_number>      Increases plant's hydration level
  
  --weeding <field_number> --plant <PLANT>  Kill weed on the field and add new plant on its place
  
  --plant <PLANT>               Add new plant
  
  --killplant <field_number>    Erase plant from the field
  
  --init                        Ignore loading state and create the garden with random 3 fields
  
  --show                        Show garden

```
