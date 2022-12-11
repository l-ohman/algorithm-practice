// input: an empty array (fn is a method on a class object)
// output: original array modified to contain all node names ordered by depth

class GraphNode {
  constructor(name) {
    this.name = name;
    this.children = [];
  }
  addChild(name) {
    this.children.push(new GraphNode(name));
    return this;
  }
  depthFirstSearch(array) {
    array.push(this.name);
    for (let i = 0; i < this.children.length; i++) {
      this.children[i].depthFirstSearch(array);
    }
    return array;
  }
}

module.exports = GraphNode;
