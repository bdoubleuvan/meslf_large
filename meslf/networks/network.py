"""
Base classes needed to create a network. Includes Network, Node, Link, and HalfLink.
"""

import abc

# %% Network

class Network(metaclass=abc.ABCMeta):
    """
    Base network class.
    
    Attributes
    ----------
    name : str
        The name of the network.
    nodes : list
        List of nodes in the network.
    links : list
        List of links in the network.
    half_links : list
        List of half links in the network.
    number_of_nodes : list
        Amount of node present in the network.
    number_of_links : list
        Amount of links present in the network.
    number_of_half_links : list
        Amount of half links present in the network.
    networks : list
        List of (sub)networks in the network.
    F_entries : list
        List of network elements corresponding to equations in the system.
    x_entries : list
        List of network elements corresponding to variables present in system of equations.
    """
    
    def __init__(self, name):
        """
        Creates a Network object.

        Parameters
        ----------
        name : str
            name of the network
        """
        super().__init__()
        
        self.name = name  # network name
        
        self.nodes = []  # list of nodes in the network
        self.links = []  # list of links in the network
        self.half_links = []  # list of half links in the network
        
        self.number_of_nodes = 0
        self.number_of_links = 0
        self.number_of_half_links = 0
        
        self.networks = []  # list of subnetworks in the network
               
        self.F_entries = []
        self.x_entries = []
        
        self.F_start_index = 0
        self.F_end_index = 0
        self.x_start_index = 0
        self.x_end_index = 0
    
      
    def add_node(self, node, position=None):
        """
        Adds node to the network, i.e. adds node to list of nodes.

        Parameters
        ----------
        node : Node
            Node object to be added to the network.
        position : integer
            Position (index) in the list of nodes of the network where the node should be inserted. 
            Default is insert at end of list.

        Raises
        ------
        TypeError
            If node is not an instance of Node.
        """
        if not isinstance(node, Node):
            raise TypeError("Only a Node object can be added.")
        
        if position is None:
            self.nodes.append(node)
        else:
            self.nodes.insert(position, node)
        
        if node.number is None:
            node.number = self.number_of_nodes  
            self.number_of_nodes += 1
    
         
    def remove_node(self, node):
        """
        Removes node from the list of nodes.
        If any links or half links are connected to that node, those links are removed as well, 
        both from the network as from the node at the other side of the link.

        Parameters
        ----------
        node : Node
            Node object to be removed from the network.

        Raises
        ------
        TypeError
            If node is not an instance of Node.
        """
        if not isinstance(node, Node):
            raise TypeError("Only a Node object can be removed.")
        
        # Remove corresponding links
        for link in node.get_links():
            if link in self.get_links():
                self.remove_link(link)
                if link in node.get_out_links():
                    link.end_node.remove_link(link)
                else:
                    link.start_node.remove_link(link)
                self.number_of_links -= 1
        
        # Remove corresponding half links
        for hl in node.get_half_links():
            if link in self.get_half_links():
                self.remove_half_link(hl)
                self.number_of_half_links -= 1
        
        self.nodes.remove(node)
        self.number_of_nodes -= 1
        
  
    def get_nodes(self, bc_types=[]):
        """
        Iterates over all the nodes in the list of nodes.
        
        Parameters
        ----------
        bc_types : list
            A list containing the identifiers of the known variables. If empty, all the nodes are yielded. 
            Default is an empty list.

        Yields
        ------
        node : Node
            The next Node instance in self.nodes.
        """
        if bc_types:
            for node in self.nodes:
                if node is not None:
                    if node.bc_type in bc_types:
                        yield node
        else:
            for node in self.nodes:
                if node is not None:
                    yield node
  
        
    def add_link(self, link, position=None):
        """
        Adds link to the list of links.
        If the start node or the end node are not yet added to the network, 
        they will be added to the list of nodes.

        Parameters
        ----------
        link : Link
            Link object to be added to the network.
        position : integer
            Position (index) in the list of links of the network where the link should be inserted. 
            Default is insert at end of list.

        Raises
        ------
        TypeError
            If link is not an instance of Link.
        """
        if not isinstance(link, Link):
            raise TypeError("Only a Link object can be added.")
        
        if position is None:
            self.links.append(link)
        else:
            self.links.insert(position, link)
        
        link.number = self.number_of_links
        self.number_of_links += 1
        
        # if link.start_node not in self.nodes:
        #     self.add_node(link.start_node)
        
        # if link.end_node not in self.nodes:
        #     self.add_node(link.end_node)
           
            
    def remove_link(self, link):
        """
        Removes link from the list of links.

        Parameters
        ----------
        link : Link
            Link object to be removed from the network.

        Raises
        ------
        TypeError
            If link in not an instance of Link.
        """
        if not isinstance(link, Link):
            raise TypeError("Only a Link object can be removed.")
        
        self.links.remove(link)
        self.number_of_links -= 1
        

    def get_links(self, link_types=[], bc_types=[], exclude_link_types=[], exclude_bc_types=[]):
        """
        Iterates over all the links in the list of links.
        This only includes links, not half links.

        Parameters
        ----------
        link_types : list
            List of link types of the links to be yielded. If empty, all the links are yielded. 
            Default is an empty list.
        bc_types : list
            A list containing the identifiers of the known variables. If empty, all the links are yielded. 
            Default is an empty list.
        exclude_link_types : list
            List of link_types to exclude. If empty, all the links are yielded.
            Default is an empty list.
        exclude_bc_types : list
            List of bc_types to exclude. If empty, all the links are yielded.
            Default is an empty list.

        Yields
        ------
        link : Link
            The next Link instance in self.links.
        """
        if link_types and bc_types:
            for link in self.links:
                if link is not None:
                    if (link.link_type in link_types) and (link.bc_type in bc_types):
                        yield link
        elif link_types and exclude_bc_types:
            for link in self.links:
                if link is not None:
                    if (link.link_type in link_types) and (link.bc_type not in exclude_bc_types):
                        yield link
        elif link_types:
            for link in self.links:
                if link is not None:
                    if link.link_type in link_types:
                        yield link
        elif bc_types:
            for link in self.links:
                if link is not None:
                    if link.bc_type in bc_types:
                        yield link
        elif exclude_link_types and exclude_bc_types:
            for link in self.links:
                if link is not None:
                    if (link.link_type not in link.exclude_link_types) and (link.bc_type not in exclude_bc_types):
                        yield link
        elif exclude_link_types:
            for link in self.links:
                if link is not None:
                    if link.link_type not in exclude_link_types:
                        yield link
        elif exclude_bc_types:
            for link in self.links:
                if link is not None:
                    if link.bc_type not in exclude_bc_types:
                        yield link
        else:
            for link in self.links:
                if link is not None:
                        yield link

 
    def add_half_link(self, half_link, position=None):
        """
        Adds half link to the list of half links.

        If the start node is not yet added to the network, 
        it will be added to the list of nodes.

        Parameters
        ----------
        half_link : HalfLink
            Half link object to be added to the network.
        position : integer
            Position (index) in the list of half links of the network where the half link should be inserted.

        Raises
        ------
        TypeError
            If half_link is not an instance of HalfLink.
        """
        if not isinstance(half_link, HalfLink):
            raise TypeError("Only a HalfLink object can be added.")
        
        # if not (half_link in self.half_links):
        if position is None:
            self.half_links.append(half_link)
        else:
            self.half_links.insert(position, half_link)
        
        half_link.number = self.number_of_half_links
        self.number_of_half_links += 1
        
        # if half_link.start_node not in self.nodes:
        #     self.add_node(half_link.start_node)
         
            
    def remove_half_link(self, half_link):
        """
        Removes half_links from the list of half links of the network.

        Parameters
        ----------
        half_link : HalfLink
            Half link object to be removed from the network.

        Raises
        ------
        TypeError
            If half_link is not an instance of HalfLink.
        """
        if not isinstance(half_link, HalfLink):
            raise TypeError("Only a HalfLink object can be removed")
        
        if half_link in self.half_links:
            self.half_links.remove(half_link)
            half_link.start_node.half_links.remove(half_link)
            self.number_of_half_links -= 1

                    
    def get_half_links(self, link_types=[], bc_types=[]):
        """
        Iterates over all the half links in the list of half links
                
        Parameters
        ----------
        link_types : list
            List of half link types of the links to be yielded. 
            If empty, all the links are yielded. Default is an empty list.
        bc_types : list
            A list containing the identifiers of the known variables.
            If empty, all half links are yielded. Default is an empty list.

        Yields
        ------
        hl : HalfLink
            The next HalfLink instance in self.half_links.
        """
        if link_types and bc_types:
            for hl in self.half_links:
                if hl is not None:
                    if (hl.link_type in link_types) and (hl.bc_type in bc_types):
                        yield hl
        elif link_types:
            for hl in self.half_links:
                if hl is not None:
                    if hl.link_type in link_types:
                        yield hl
        elif bc_types:
            for hl in self.half_links:
                if hl is not None:
                    if hl.bc_type in bc_types:
                        yield hl
        else:
            for hl in self.half_links:
                if hl is not None:
                    yield hl
       
                
    def add_network(self, network):
        """
        Adds network to the network nlist.
        
        Parameters
        ----------
        network : Network
            The network to be added.

        Raises
        ------
        TypeError
            If network is not a Network instance.
        """
        if not isinstance(network, Network):
            raise TypeError("Only a Network object can be added.")
                
        self.networks.append(network)
     
     
    def get_networks(self):
        """
        Iterates over all the networks in the list of networks.

        Yields
        ------
        net : Network
            The next Network instance in self.networks.
        """
        for network in self.networks:
            if network is not None:
                yield network
          
                        
    @abc.abstractmethod
    def initialize(self):
        """
        Initalizes the network. To be specified for every subclass of Network.
        """
        pass
    
        
    @abc.abstractmethod
    def set_x_entries(self):
        """
        Yelds all the nodes, links, and half links that have an entry in variable vector x.
        """
        pass
    
     
    def get_x_entries(self):
        """
        Returns all the nodes, links, and half links that have an entry in variable vector x.
        """
        for element in self.x_entries:
            if element is not None:
                yield element


    @abc.abstractmethod
    def set_F_entries(self):
        """
        Returns all the nodes, links, and half links that have an entry in function vector F.
        """
        pass


    def get_F_entries(self):
        """
        Yields all the nodes, links, and half links that have an entry in variable vector x.
        """
        for element in self.F_entries:
            if element is not None:
                yield element

    
    @abc.abstractmethod
    def update(self, x):
        """
        Update the network for given variable vector x. To be specified for every subclass of Network.
        """
        pass
    
    
    @abc.abstractmethod
    def update_full(self, x):
        """
        Updates the full network given variable vector x.
        Unlike update(x), not only the values from x are updated, 
        but also all parameters not included in x.

        Returns the full set of network state parameters.
        """
        pass
    
    
    @abc.abstractmethod
    def solve_network(self):
        """
        Gives the solution throughout the entire network of steady-state load flow analysis.

        To be specified for every subclass of Network.
        """
        pass
    
# %% Node

class Node(metaclass=abc.ABCMeta):
    """
    Base node class.
    
    Attributes
    ----------
    name : str
        The name of the node.
    number : int
        Number of the node.
    scale_var : string
        How to scale the variable. Default is no scaling.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    in_links : list
        List of ingoing links connected to the node, except half links.
    out_links : list
        List of outgoing links connected to the node, except half links.
    half_links : list
        List of half links connected to the node.
    """

    def __init__(self, name, number=None, scale_var=None, scale_var_params=None):
        """
        Creates a Node object.

        Parameters
        ----------
        name : str
            The name of the node.
        number : int
            Number of the node.
        scale_var : string
            How to scale the variable. Default is no scaling. Alternative option is 'per_unit'.
        scale_var_params : dict
            Dictionary with values needed for scaling variables. Default is None.  
        """
        super().__init__()
        
        self.name = name
        self.number = number
        
        self.out_links = []
        self.in_links = []
        self.half_links = []
        
        self.scale_var = scale_var
        self.scale_var_params = scale_var_params


    def get_out_links(self, bc_types=[]):
        """
        Iterates over all the outgoing links connected to the node.
        
        Parameters
        ----------
        bc_types : list
            A list containing the identifiers of the known variables.
            If empty, all links are yielded. Default is an empty list.

        Yields
        ------
        link : Link
            The next Link instance in self.out_links
        """
        if bc_types:
            for link in self.out_links:
                if link is not None:
                    if link.bc_type in bc_types:
                        yield link
        else:
            for link in self.out_links:
                if link is not None:
                    yield link


    def get_in_links(self, bc_types=[]):
        """
        Iterates over all the incoming links connected to the node.
        
        Parameters
        ----------
        bc_types : list
            A list containing the identifiers of the known variables.
            If empty, all links are yielded. Default is an empty list.

        Yields
        ------
        link : Link or HalfLink
            The next Link instance in self.in_links.
        """
        if bc_types:
            for link in self.in_links:
                if link is not None:
                    if link.bc_type in bc_types:
                        yield link
        else:
            for link in self.in_links:
                if link is not None:
                    yield link


    def get_half_links(self, link_types=[], bc_types=[]):
        """
        Iterates over all the half links connected to the node.

        Parameters
        ----------
        link_types : list
            List of half link types of the links to be yielded. 
            If empty, all the links are yielded. Default is an empty list.
        bc_types : list
            A list containing the identifiers of the known variables.
            If empty, all half links are yielded. Default is an empty list.

        Yields
        ------
        hl : HalfLink
            The next HalfLink instance in self.half_links.
        """
        if link_types and bc_types:
            for hl in self.half_links:
                if hl is not None:
                    if (hl.link_type in link_types) and (hl.bc_type in bc_types):
                        yield hl
        elif link_types:
            for hl in self.half_links:
                if hl is not None:
                    if hl.link_type in link_types:
                        yield hl
        elif bc_types:
            for hl in self.half_links:
                if hl is not None:
                    if hl.bc_type in bc_types:
                        yield hl
        else:
            for hl in self.half_links:
                if hl is not None:
                    yield hl


    def get_links(self):
        """
        Iterates over all the links connected to the node; incoming, outgoing and half links.

        Yields
        ------
        link : Link or HalfLink
            The next Link or HalfLink instance.
        """
        for link in self.out_links + self.in_links + self.half_links:
            if link is not None:
                yield link


    def remove_link(self, link):
        """
        Removes link from the list of out links or the list of in links.

        Parameters
        ----------
        link : Link
            Link to be removed from the node.

        Raises
        ------
        TypeError
            If link is not an instance of Link.
        """
        if not isinstance(link, Link):
            raise TypeError("Only a Link object can be removed.")
        
        if link in self.out_links:
            self.out_links.remove(link)
        elif link in self.in_links:
            self.in_links.remove(link)


    def remove_half_link(self, half_link):
        """
        Removes half_link from the list of half links and the list of out links.

        Parameters
        ----------
        half_link : HalfLink
            Half link to be removed from the node.

        Raises
        ------
        TypeError
            If half_link is not an instance of HalfLink.
        """
        if not isinstance(half_link, HalfLink):
            raise TypeError("Only a HalfLink object can be removed.")
        
        self.half_links.remove(half_link)


    @abc.abstractmethod
    def node_law(self):
        """
        Node law.
        """
        pass
    
# %% Link

class Link(metaclass=abc.ABCMeta):
    """
    Base link class.
    
    Attributes
    ----------
    name : str
        The name of the link.
    start_node : Node
        Start node of the link.
    end_node : Node
        End node of the link.
    number : int
        Number of the link.
    scale_var : string
        How to scale the variable.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    """

    def __init__(self, name, start_node, end_node, number=None, scale_var=None, scale_var_params=None):
        """
        Creates a Link object

        Parameters
        ----------
        name : str
            The name of the link.
        start_node : Node
            Start node of the link.
        end_node : Node
            End node of the link.
        number : int
            Number of the link.
        scale_var : string
            How to scale the variable.
        scale_var_params : dict
            Dictionary with values needed for scaling variables.

        Raises
        ------
        TypeError
            If start_node or end_node is not an instance of Node.
        """
        if not isinstance(start_node, Node):
            raise TypeError("Only a Node object can be a start node.")
        
        if not isinstance(end_node, Node):
            raise TypeError("Only a Node object can be an end node.")
        
        super().__init__()
        
        self.name = name
        self.number = number
        
        self.start_node = start_node
        start_node.out_links.append(self)
        
        self.end_node = end_node
        end_node.in_links.append(self)
        
        self.scale_var = scale_var
        self.scale_var_params = scale_var_params
        
# %% Half link

class HalfLink(metaclass=abc.ABCMeta):
    """
    Base half link class. A half link is by default considered as an outflowing link.
    
    Attributes
    ----------
    name : str
        Name of the half link.
    start_node : Node
        Start node of the half link.
    number : int
        Number of the half link.
    scale_var : string
        How to scale the variable.
    scale_var_params : dict
        Dictionary with values needed for scaling variables.
    """

    def __init__(self, name, start_node, number=None):
        """
        Creates a HalfLink object

        Parameters
        ----------
        name : str
            Name of the half link.
        start_node : Node
            Start node of the half link.
        number : int
            Number of the half link.

        Raises
        ------
        TypeError
            If start_node is not an instance of Node.
        """
        if not isinstance(start_node, Node):
            raise TypeError("Only a Node object can be a start node.")
        
        super().__init__()
        
        self.name = name
        self.number = number
        
        self.start_node = start_node
        start_node.half_links.append(self)
        
        self.scale_var = start_node.scale_var
        self.scale_var_params = start_node.scale_var_params