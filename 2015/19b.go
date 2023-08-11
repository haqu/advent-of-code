package main

import (
    "os"
    "log"
    "strings"
    "regexp"
)

const test_data = `
e => H
e => O
H => HO
H => OH
O => HH

HOH
`

type Node struct {
    text   string
    depth  int
    parent *Node
    nodes  []*Node
}

var (
    molecule     string
    replacements [][]string
    root         *Node
)

func get_data(is_test bool) []string {
    if is_test {
        return strings.Split(strings.TrimSpace(test_data),"\n")
    } else {
        data,err := os.ReadFile("19.txt")
        if err != nil {
            log.Fatal(err)
        }
        return strings.Split(string(data),"\n")
    }
}

func create_node(text string) *Node {
    var n Node
    n.text = text
    n.depth = 0
    return &n
}

func add_node(parent *Node,text string) *Node {
    n := create_node(text)
    n.depth = parent.depth+1
    n.parent = parent
    parent.nodes = append(parent.nodes,n)
    return n
}

func grow_tree(n *Node) {
    if n.text == "e" {
        log.Print("done, depth: ",n.depth)
        os.Exit(0)
    }
    for _,r := range replacements {
        re := regexp.MustCompile(r[0])
        arr := re.FindAllIndex([]byte(n.text),-1)
        if len(arr) == 0 {
            continue
        }
        for _,pair := range arr {
            p1 := pair[0]
            p2 := pair[1]
            variation := ""
            if p1 >= 0 {
                variation += n.text[:p1]
            }
            variation += r[1]
            if p2 <= len(n.text)-1 {
                variation += n.text[p2:]
            }
            n2 := add_node(n,variation)
            grow_tree(n2)
        }
    }
}

func main() {
    lines := get_data(false)
    next_line_is_molecule := false
    for _,line := range lines {
        if line == "" {
            next_line_is_molecule = true
            continue
        }
        if !next_line_is_molecule {
            parts := strings.Split(line," => ")
            replacements = append(replacements,[]string{parts[1],parts[0]}) // reverse
        } else {
            molecule = line
        }
    }
    log.Print("molecule: ",molecule)
    root = create_node(molecule)
    grow_tree(root)
}

