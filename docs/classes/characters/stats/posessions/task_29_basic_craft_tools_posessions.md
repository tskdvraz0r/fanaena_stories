# TASK 29: Реализовать класс **"BasicCraftToolsPosessions"**;
## 1. Описание;
Реализовать класс **"BasicCraftToolsPosessions"**, отвечающий за владения персонажем инструментами ремесленника.


## 1. Атрибуты класса;
*Атрибуты* класса не предусмотрены:


## 2. Свойства класса;
*Свойства* класса не предусмотрены.


## 3. Методы класса;
*Методы* класса не предусмотрены.


## 4. Инициализация экземпляра класса;
При инициализации экземпляра класс должен принимать следующие *аргументы*:
* class_profession: BasicProfession - экземпляр класса "Профессии" персонажа;


## 5. Атрибуты экземпляра класса;
Экземпляр класса должен иметь следующие *атрибуты*:
* class_profession: BasicProfession - экземпляр класса "Профессии" персонажа;
* self._alchemists_supplies: bool - владение инструментами алхимика;
* self._artisans_tools: bool - владение инструментами ремесленника;
* self._brewer_tools: bool - владение инструментами пивовара;
* self._calligraphers_supplies: bool - владение инструментами каллиграфа;
* self._carpenter_tools: bool - владение инструментами плотника;
* self._cartographer_tools: bool - владение инструментами картографа;
* self._cobblers_tools: bool - владение инструментами сапожника;
* self._cooks_utensils: bool - владение инструментами повара;
* self._glass_blower_tools: bool - владение инструментами стеклодува;
* self._jeweler_tools: bool - владение инструментами ювелира;
* self._letherworker_tools: bool - владение инструментами кожевника;
* self._masons_tools: bool - владение инструментами каменщика;
* self._painters_supplies: bool - владение инструментами художника;
* self._potter_tools: bool - владение инструментами гончара;
* self._smiths_tools: bool - владение инструментами кузнеца;
* self._tinkers_tools: bool - владение инструментами ремонтника;
* self._weaver_tools: bool - владение инструментами ткача;
* self._wood_carver_tools: bool - владение инструментами резчика по дереву;


## 6. Свойства экземпляра класса;
Экземпляр класса должен иметь следующие *свойства*:
* alchemists_supplies - геттер и сеттер;
* artisans_tools - геттер и сеттер;
* brewer_tools - геттер и сеттер;
* calligraphers_supplies - геттер и сеттер;
* carpenter_tools - геттер и сеттер;
* cartographer_tools - геттер и сеттер;
* cobblers_tools - геттер и сеттер;
* cooks_utensils - геттер и сеттер;
* glass_blower_tools - геттер и сеттер;
* jeweler_tools - геттер и сеттер;
* letherworker_tools - геттер и сеттер;
* masons_tools - геттер и сеттер;
* painters_supplies - геттер и сеттер;
* potter_tools - геттер и сеттер;
* smiths_tools - геттер и сеттер;
* tinkers_tools - геттер и сеттер;
* weaver_tools - геттер и сеттер;
* wood_carver_tools - геттер и сеттер;

## 7. Методы экземпляра класса;
Экземпляр класса должен иметь следующие *методы*:
* choice_craft_tools_posessions - Метод считывает из экземпляра класса Профессии данные по владению инструментами ремесленника и меняет статус с False на True.
