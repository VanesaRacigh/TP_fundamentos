#!/bin/bash/python
# -*- coding: utf-8 -*-

class Elemento():
	def __init__(self,cantProtones,cantNeutrones,valencia,simbolo):
		self.cantProtones=cantProtones
		self.cantNeutrones=cantNeutrones
		self.valencia=valencia
		self.simbolo=simbolo
		self.cantElectrones=cantProtones
		self.numeroAtomico=cantProtones
		self.pesoAtomico=(cantProtones+cantNeutrones)

class TablaPeriodica():
	def __init__(self):
		self.lista=[]
	def agregarElemento(self,elemento):
		self.lista.append(elemento)
	def elementos(self):
		return self.lista
	def elementoS(self,sim):
		for ele in self.lista:
			if (ele.simbolo == sim): 		
				return ele			
	def elementoN(self,numero):
		for ele in self.lista:
			if (ele.cantProtones == numero):		
				return ele
			
class Compuesto():

	def __init__(self):
		self.atomos=[]
		self.nombres=[]
		self.enlaces=[]
		self.total_enlaces=0

	def agregarAtomo(self, elemento, nombre):
		self.atomos.append(elemento)
		self.nombres.append(nombre)

	def enlazar(self, nombre1,nombre2):
		self.total_enlaces += 1
		self.enlaces.append(nombre1)
		self.enlaces.append(nombre2)

	def cantAtomos(self):
		return len(self.atomos)

	def cantEnlaces(self):
		return self.total_enlaces

	def incluyeAtomo (self,nombre):
		return (nombre in self.nombres)

	def incluyeElemento(self,elemento):
		return (elemento in self.atomos) 

	def atomosDe(self,elemento):
		lista=[]
		name=[[a,n] for a,n in zip(self.atomos,self.nombres)] 
		for par in name:
			if par[0]==elemento:
				lista.append(par[1])	
		return lista

	def cantEnlacesAtomo(self,nombre):
		return self.enlaces.count(nombre)
	def elementosPresentes(self):
		solo_tipo=[]
		for x in self.atomos:
			if x in solo_tipo:
				pass
			else:
				solo_tipo.append(x)
		return solo_tipo

	def masaMolar(self):
		masa=0
		for element in self.atomos:
			masa += element.pesoAtomico
		return masa
		
	def proporcionSobreMasa(self,elemento):
		masa=0
		for element in self.atomos:
			masa += element.pesoAtomico
		proporcion= elemento.pesoAtomico/float(masa)
		return float("{:.4f}".format(proporcion)) #para que el test no falle


class Medio():

	def __init__(self):
		self.componentes=[]
		self.cantidades=[]	

	def agregarComponente(self,sustancia,cant):
		if sustancia in self.componentes:
			posicion=self.componentes.index(sustancia)
			self.cantidades [posicion] += cant
		else:		
			self.componentes.append(sustancia)
			self.cantidades.append(cant)

	def masaTotal(self):
		masa_molar=[]
		for sustancia in self.componentes:
			masa_molar.append(sustancia.masaMolar())
		a=[a*b for a,b in zip(masa_molar,self.cantidades)] 
		masaTotal=0		
		for valor in a:
			masaTotal += valor
		return masaTotal

	def elementosPresentes(self):
		solo_tipo=[]
		for sustancia in self.componentes:
			for atm in sustancia.atomos:
				if atm in solo_tipo:
					pass
				else:
					solo_tipo.append(atm)
		return solo_tipo 
				

	def compuestosPresentes(self):
		return self.componentes		
		 
	def cantMolesElemento(self,elemento):
		numero=[] 
		for componente in self.componentes:
			numero.append(componente.atomos.count(elemento))
		moles_por_componente=[a*b for a,b in zip(self.cantidades,numero)]
		moles_total=0		
		for valor in moles_por_componente:
			moles_total += valor
		return moles_total


	def masaDeElemento(self,elemento):
		numero=[] 
		for componente in self.componentes:
			numero.append(componente.atomos.count(elemento))
		masa_por_componente=[(elemento.pesoAtomico)*(a*b) for a,b in zip(self.cantidades,numero)]
		masa_total=0		
		for valor in masa_por_componente:
			masa_total += valor
		return masa_total
	
	def masaDeCompuesto(self,sustancia):
		p= self.componentes.index(sustancia)
		masa_compuesto= sustancia.masaMolar() * self.cantidades[p]
		return masa_compuesto

	def proporcionCompuestoSobreMasa(self,compuesto):
		c= float(self.masaDeCompuesto(compuesto))/float(self.masaTotal())
		return float("{:.4f}".format(c))
	def proporcionElementoSobreMasa(self,elemento):
	 	c= float(self.masaDeElemento(elemento))/float(self.masaTotal())
		return float("{:.4f}".format(c)) #ésto redondea, no trunca. Entonces el test da error.
	






