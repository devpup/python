class Game:
    title = ''

    def __init__(self, tag):
        #self.title = c.select('div.WsMG1c')[0].get('title')
        self.title = self.get_attr(tag, 'div.WsMG1c', 'title')
        #self.comp = c.select('div.KoLSrc')[0].text
        self.comp = self.get_text(tag, 'div.KoLSrc')
        
        rating_tag = self.get_tag(tag, 'div.pf5lIe > div')
        #rating_tag = self.get_tag(tag, 'div aria-label')        
        #print(">>>>", len(rating_tag), type(rating_tag), rating_tag)
        #rating_tag.get('')
        s_rating = rating_tag.get('aria-label').strip()
        #print(">>>>", type(s_rating), s_rating)
        self.rating = float(s_rating.split(' ')[1])

        #price_tag = self.get_tag(tag, 'span.VfPpfd > span')
        #print(price_tag)
        self.price = float(self.get_text(tag, 'span.VfPpfd > span').replace('$',''))
        #print("price >>>", self.price)

        t_url = self.get_tag(tag, 'div.wXUyZd > a')
        s_url = t_url.get('href').strip()
        #self.url = self.get_text(tag, 'div.wXUyZd > a')
        print("url >>>>", s_url) 
        
 
        
    
    def get_text(self, parent_tag, selector):
        t = self.get_tag(parent_tag, selector)
        #print(">>>>>> t", len(t), t.text)
        return "" if t == None or len(t) == 0 else t.text.strip()
        
    
    def get_attr(self, parent_tag, selector, attr_name):
        t = self.get_tag(parent_tag, selector)
        return "" if t == None or len(t) == 0 else t.get(attr_name).strip()
        #self.title = c.select('div.WsMG1c')[0].get('title')

    def get_tag(self, parent_tag, selector):
        t = parent_tag.select(selector)        
        return None if t == None or len(t) == 0 else t[0]
        #title = c.select('div.WsMG1c')[0].text
    
    def __str__(self):        
        return self.to_str()

    def to_str(self):
        return "{} {} {} ${:.1f}".format(self.title.encode('unicode-escape'), self.comp.encode('unicode-escape'), self.rating, self.price)

