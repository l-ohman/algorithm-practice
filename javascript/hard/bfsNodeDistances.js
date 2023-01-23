// hard, BFS
// currently only passes first test of 8

class Node {
  constructor(value) {
    this.value = value;
    this.edges = [];
    this.distanceFromS = -1;
  }
  addChild(node) {
    this.edges.push(node);
  }
  setDistance(x) {
    this.distanceFromS = x;
  }
}

function bfs(n, m, edges, s) {
  // create array of all input nodes
  const nodes = [];
  for (let i = 0; i < n; i++) {
    nodes.push(new Node(i + 1));
  }

  // create edges for all nodes
  for (let i = 0; i < m; i++) {
    nodes[edges[i][0] - 1].addChild(nodes[edges[i][1] - 1]);
    nodes[edges[i][1] - 1].addChild(nodes[edges[i][0] - 1]);
  }

  let nodesVisited = [s];
  function checkEdgesAndSetDistance(node) {
    for (let i = 0; i < node.edges.length; i++) {
      nodesVisited.push(node.edges[i].value);

      const distance = node.edges[i].distanceFromS;
      if (distance === -1) {
        node.edges[i].setDistance(6);
      } else {
        node.edges[i].setDistance(distance + 6);
      }

      if (nodesVisited.find((j) => j === node.value)) continue;
      else checkEdgesAndSetDistance(node.edges[i]);
    }
  }
  nodes[s - 1].setDistance = 0;
  checkEdgesAndSetDistance(nodes[s - 1]);

  const distances = nodes.map((node) => node.distanceFromS);
  distances.splice(s - 1, 1);
  return distances;
}
