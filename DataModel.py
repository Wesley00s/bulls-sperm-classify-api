from pydantic import BaseModel


class Data(BaseModel):
    idade: int
    peso: int
    ec: float
    ce: float
    temp_retal: float
    temp_amb: float
    umidade: float
    mov_flanco: float
    turbilhao: float
    mot_moveis: float
    vigor: float
    volume: float
    zptz_106: float
    # zptz_totais: float
    def_mai: float
    def_mai_percent: float
    # def_men: float
    # def_men_percent: float
    normais: float
    normais_percent: float
