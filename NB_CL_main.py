#coding=utf-8
from algorithms import NaiveBayes as NB
from algorithms import ChowLiu as CL
from plot import plotTools

def testNB():
	classfier = NB.NaiveBayes()
	classfier.train()
	classfier.predict()

def testCL():
	cl = CL.ChowLiu()
	cl.calMI()
	cl.kruskal()
	plotTools.plotGraph(cl.nodeEdges, cl.XCloumns)

if __name__ == '__main__':
	#testNB()
	testCL()