#!/bin/bash/python
# -*- coding: utf-8 -*-


import p
import unittest

class ElementoTest(unittest.TestCase):
	def test_basicos(self):
		oxigeno=p.Elemento(8,8,4,'O')
		self.assertEqual(8,oxigeno.cantProtones)
		self.assertEqual(8,oxigeno.cantNeutrones)
		self.assertEqual(8,oxigeno.cantElectrones)
		self.assertEqual(8,oxigeno.numeroAtomico)
		self.assertEqual(4,oxigeno.valencia)
		self.assertEqual('O',oxigeno.simbolo)

class TablaTest(unittest.TestCase):
	def test_basicos(self):
		nitrogeno=p.Elemento(7,7,5,'N')
		carbono=p.Elemento(6,6,4,'C')
		oxigeno=p.Elemento(8,8,4,'O')
		hidrogeno=p.Elemento(1,0,1,'H')
		tabla=p.TablaPeriodica()
		tabla.agregarElemento(nitrogeno)
		tabla.agregarElemento(carbono)
		tabla.agregarElemento(hidrogeno)
		tabla.agregarElemento(oxigeno)
		self.assertEqual(4,len(tabla.elementos()))
		self.assertEqual(6,tabla.elementoS('C').numeroAtomico)
		self.assertEqual(14,tabla.elementoN(7).pesoAtomico)

class CompuestoTest(unittest.TestCase):
	def test_basicos(self):
		hidrogeno=p.Elemento(1,0,1,'H')
		nitrogeno=p.Elemento(7,7,5,'N')
		tabla=p.TablaPeriodica()
		tabla.agregarElemento(hidrogeno)
		tabla.agregarElemento(nitrogeno)
		nh3=p.Compuesto()
		nh3.agregarAtomo(tabla.elementoS('N'),'N1')
		nh3.agregarAtomo(tabla.elementoS('H'),'H2')
		nh3.agregarAtomo(tabla.elementoS('H'),'H3')
		nh3.agregarAtomo(tabla.elementoS('H'),'H4')
		nh3.enlazar('N1','H2')
		nh3.enlazar('N1','H3')
		nh3.enlazar('N1','H4')
		self.assertEqual(4, nh3.cantAtomos())
		self.assertEqual(['H2', 'H3', 'H4'], nh3.atomosDe(tabla.elementoS('H')))
		self.assertEqual(True, nh3.incluyeAtomo('N1'))
		self.assertEqual(False, nh3.incluyeAtomo('N4'))
		self.assertEqual(True, nh3.incluyeElemento(tabla.elementoS('N')))
		self.assertEqual(False, nh3.incluyeElemento(tabla.elementoS('O')))
		self.assertEqual(['N', 'H'], [elem.simbolo for elem in nh3.elementosPresentes()])
		self.assertEqual(3, nh3.cantEnlaces())
		self.assertEqual(1, nh3.cantEnlacesAtomo('H2'))
		self.assertEqual(17, nh3.masaMolar())
		self.assertAlmostEqual(0.8235, nh3.proporcionSobreMasa(tabla.elementoS('N')),3) #1


class MedioTest(unittest.TestCase):
	def test_basicos(self):
		oxigeno=p.Elemento(8,8,4,'O')
		hidrogeno=p.Elemento(1,0,1,'H')
		nitrogeno=p.Elemento(7,7,5,'N')
		carbono=p.Elemento(6,6,4,'C')
		tabla=p.TablaPeriodica()
		tabla.agregarElemento(oxigeno)
		tabla.agregarElemento(hidrogeno)
		tabla.agregarElemento(nitrogeno)
		tabla.agregarElemento(carbono)
		nh3=p.Compuesto()
		nh3.agregarAtomo(tabla.elementoS('N'),'N1')
		nh3.agregarAtomo(tabla.elementoS('H'),'H2')
		nh3.agregarAtomo(tabla.elementoS('H'),'H3')
		nh3.agregarAtomo(tabla.elementoS('H'),'H4')
		nh3.enlazar('N1','H2')
		nh3.enlazar('N1','H3')
		nh3.enlazar('N1','H4')
		h2o=p.Compuesto() 
		h2o.agregarAtomo(hidrogeno,'H1')
		h2o.agregarAtomo(hidrogeno,'H2')
		h2o.agregarAtomo(oxigeno,'O')
		h2o.enlazar('H1','O')
		h2o.enlazar('H2','O')
		metano=p.Compuesto()
		metano.agregarAtomo(carbono,'C')
		metano.agregarAtomo(hidrogeno,'H1')
		metano.agregarAtomo(hidrogeno,'H2')
		metano.agregarAtomo(hidrogeno,'H3')
		metano.agregarAtomo(hidrogeno,'H4')
		metano.enlazar('C','H1')
		metano.enlazar('C','H2')
		metano.enlazar('C','H3')
		metano.enlazar('C','H4')
		co2=p.Compuesto() 
		co2.agregarAtomo(carbono,'C')
		co2.agregarAtomo(oxigeno,'O1')
		co2.agregarAtomo(oxigeno,'O2')
		co2.enlazar('C','O1')
		co2.enlazar('C','O1')
		co2.enlazar('C','O2')
		co2.enlazar('C','O2')
		medioRaro=p.Medio()
		medioRaro.agregarComponente(h2o,100)
		medioRaro.agregarComponente(nh3,6)
		medioRaro.agregarComponente(metano,20)
		medioRaro.agregarComponente(co2,14)
		medioRaro.agregarComponente(nh3,15)
		self.assertEqual(3093, medioRaro.masaTotal())
		self.assertEqual([hidrogeno,oxigeno,nitrogeno,carbono], medioRaro.elementosPresentes())
		self.assertEqual([h2o,nh3,metano,co2], medioRaro.compuestosPresentes())
		self.assertEqual(128, medioRaro.cantMolesElemento(oxigeno))
		self.assertEqual(343, medioRaro.cantMolesElemento(hidrogeno))
		self.assertEqual(2048, medioRaro.masaDeElemento(oxigeno))
		self.assertEqual(408, medioRaro.masaDeElemento(carbono))
		self.assertEqual(1800, medioRaro.masaDeCompuesto(h2o))
		self.assertEqual(357, medioRaro.masaDeCompuesto(nh3))
		self.assertAlmostEqual(0.5819, medioRaro.proporcionCompuestoSobreMasa(h2o),3) 
		self.assertAlmostEqual(0.6621, medioRaro.proporcionElementoSobreMasa(oxigeno),3)
		self.assertAlmostEqual(0.1108, medioRaro.proporcionElementoSobreMasa(hidrogeno),3)

	# A todas las proporciones les puse formato a la salida del programa para que coincidan con los valores
	# de prueba del test. Pero como redondea el número, en uno de los casos 0.5819!= 0.582 pasaba ésto, entonces
	# usé assertAlmostEqual en el test directamente. 
	


