class Edge:
    def __init__(self, id, name=None, length=None, coverage=None, multiplicity=None,
                 color=None, chrom=None, repetitive=False, element_id=None):
        self.id = id
        self.element_id = element_id
        self.name = name
        self.length = length
        self.cov = coverage
        self.start = None
        self.end = None
        self.is_complex_loop = False
        self.multiplicity = multiplicity or 1
        self.color = color or "black"
        self.chrom = chrom or None
        self.repetitive = repetitive
        self.two_way = False
        self.component = None
        self.ref_component = None
        self.repeat_component = None

    def as_dict(self):
        return {'id': self.id, 'el_id': self.element_id, 'name': self.name, 'len': self.format_len(), 'cov': self.cov,
                's': self.start, 'e': self.end, 'mult': self.multiplicity, 'color': self.color, 'unique': not self.repetitive,
                'chrom': self.chrom, 'comp': self.component, 'rep_comp': self.repeat_component,
                'ref_comp': self.ref_component}

    def format_len(self):
        if not self.length:
            return 0
        if self.length < 5000:
            return float("%.1f" % (self.length / 1000.0))
        else:
            return int(self.length / 1000)

    def print_edge_to_dot(self):
        if self.is_complex_loop:
            s = '"%s" -> "%s" [label = "", id = "%s", color = "black", penwidth=5] ;\n' % \
                (self.start, self.end, self.id)
        else:
            l = str(self.format_len()) + 'k'
            s = '"%s" -> "%s" [label = id %s %s %dx(%d), id = "%s", color = "%s"] ;\n' % \
                (self.start, self.end, self.id, l, self.cov, self.multiplicity, self.id, self.color)
        return s