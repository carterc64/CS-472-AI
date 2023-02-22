from queue import PriorityQueue
class CityNode():

  #Node intilizer
  def __init__(self, label):
    self.label = label
    self.children = []

  #Adds child to self.chldren
  def addChildEdge(self, node, dist):
    edge = ChildEdge(self, node, dist)
    self.children.append(edge)

  #Gives node a print command format
  def __repr__(self):
    return '{}'.format(self.label)

  #Greater than less than for nodes
  def __lt__(self, toCompare):
    return self.label < toCompare.label
  def __gt__(self, toCompare):
    return self.label > toCompare.label
    
class ChildEdge():
  
  #ChildEdge intilizer
  def __init__(self, begin: CityNode, end: CityNode, dist):
    self.begin = begin
    self.end = end
    self.dist = dist
   


def ucs(begin, end):
  #Initlizes priority queue
  queue = PriorityQueue()
  queue.put([0, [begin]])
  #Prints starting city
  y = "[0, [{}]]".format(begin)
  print(y)
  #Declares list used for printing
  paths = list()
  #Prints divider for easier viewing
  y = "---------"
  print(y)
  

  while not queue.empty():

    #Gets highestPriority path
    highestPrio = queue.get()

    #Gets rid of repeat occurences in paths list by checking for repeat occurences
    #of preivous weights
    count = 0
    for item in paths:
      if item[0] == highestPrio[0]:
        del paths[count]
      count += 1

    #Get current end node from highestPrio path
    current = highestPrio[1][-1]
    #Check to see if were at the goal end node
    if current.label == end:
      print("Solution: {}".format(highestPrio[1]))
      return 
    
    for child in current.children:
      #Takes the current list of node paths
      newPath = list(highestPrio[1])
      #Skips previously visted nodes
      if newPath.count(child.end) > 0:
        continue
      #Adds the next node to the path
      newPath.append(child.end)
      #Creates newPath with new weight (old weight + child weight)
      x = [highestPrio[0] + child.dist, newPath]
      #Adds the path to paths to print
      paths.append(x)
      #Adds the new path with new weight into the queue
      queue.put(x)
    
   
    print(paths) 
    print(y)
    
    
def run():

    #Establishes nodes for map
    arad = CityNode("arad")
    timisoara = CityNode("timisoara")
    zerind = CityNode("zerind")
    oradea = CityNode("oradea")
    lugoj = CityNode("lugoj")
    sibiu = CityNode("sibiu")
    mehadia = CityNode("mehadia")
    rimnicuVilcea = CityNode("rimnicu Vilcea")
    fagaras = CityNode("fagaras")
    drobeta = CityNode("drobeta")
    craiova = CityNode("craiova")
    pitesti = CityNode("pitesti")
    bucharest = CityNode("bucharest")
    neamt = CityNode("neamt")
    iasi = CityNode("iasi")
    giurgiu = CityNode("giurgiu")
    urziceni = CityNode("urziceni")
    vaslui = CityNode("vaslui")
    hirsova = CityNode("hirsova")
    eforie = CityNode("eforie")

    #Puts those nodes in an array
    nodes = [arad,timisoara, zerind, oradea, lugoj, sibiu, mehadia, rimnicuVilcea, fagaras, drobeta, 
           craiova, pitesti, bucharest, neamt, iasi, giurgiu, urziceni, vaslui, hirsova, eforie]

    #Adds edges to nodes with weights
    arad.addChildEdge(timisoara, 118)
    arad.addChildEdge(zerind, 75)
    arad.addChildEdge(sibiu, 140)
    timisoara.addChildEdge(lugoj, 111)
    timisoara.addChildEdge(arad, 188)
    zerind.addChildEdge(arad, 75)
    zerind.addChildEdge(oradea, 71)
    oradea.addChildEdge(zerind, 71)
    oradea.addChildEdge(sibiu, 151)
    lugoj.addChildEdge(timisoara, 111)
    lugoj.addChildEdge(mehadia, 70)
    sibiu.addChildEdge(oradea, 151)
    sibiu.addChildEdge(arad, 140)
    sibiu.addChildEdge(rimnicuVilcea, 80)
    sibiu.addChildEdge(fagaras, 99)
    mehadia.addChildEdge(lugoj, 70)
    mehadia.addChildEdge(drobeta, 75)
    rimnicuVilcea.addChildEdge(sibiu, 80)
    rimnicuVilcea.addChildEdge(craiova, 146)
    rimnicuVilcea.addChildEdge(pitesti, 97)
    fagaras.addChildEdge(sibiu, 99)
    fagaras.addChildEdge(bucharest, 211)
    drobeta.addChildEdge(mehadia, 75)
    drobeta.addChildEdge(craiova, 120)
    craiova.addChildEdge(rimnicuVilcea, 146)
    craiova.addChildEdge(drobeta, 120)
    craiova.addChildEdge(pitesti, 138)
    pitesti.addChildEdge(rimnicuVilcea, 97)
    pitesti.addChildEdge(craiova, 138)
    pitesti.addChildEdge(bucharest, 101)
    bucharest.addChildEdge(pitesti, 101)
    bucharest.addChildEdge(fagaras, 211)
    bucharest.addChildEdge(urziceni, 85)
    bucharest.addChildEdge(giurgiu, 90)
    urziceni.addChildEdge(bucharest, 85)
    urziceni.addChildEdge(vaslui, 142)
    urziceni.addChildEdge(hirsova, 98)
    vaslui.addChildEdge(urziceni, 142)
    vaslui.addChildEdge(iasi, 92)
    iasi.addChildEdge(vaslui, 92)
    iasi.addChildEdge(neamt, 87)
    neamt.addChildEdge(iasi, 87)
    hirsova.addChildEdge(urziceni, 98)
    hirsova.addChildEdge(eforie, 86)
    eforie.addChildEdge(hirsova,86)

    #User input for begin and end states
    beginInput = input("Enter starting city: ").lower()
    end = input("Enter end city: ").lower()

    #Correlates the string with the correct starting node
    count = 0
    for node in nodes:
      if(beginInput == node.label):
        ucs(nodes[count], end)
      count += 1


run()

