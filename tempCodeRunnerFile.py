def minimumCardPickup(self,cards):
        maps = defaultdict(list)
        
        for i, v in enumerate(cards):
            maps[cards[i]].append(i)