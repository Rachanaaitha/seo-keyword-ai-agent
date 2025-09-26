import random

class SEOAnalyzer:
    def __init__(self):
        self.search_volume_ranges = {
            'best': (1000, 10000),
            'how to': (500, 5000),
            'for beginners': (300, 3000),
            'near me': (200, 4000),
            'review': (200, 2500),
            'cost': (400, 3500),
            'vs': (300, 2000),
            'free': (800, 6000),
            '2024': (100, 1500),
            'top 10': (600, 5000)
        }
    
    def analyze(self, keywords):
        analyzed_keywords = []
        
        for keyword in keywords:
            search_volume = self._estimate_search_volume(keyword)
            competition = self._estimate_competition(keyword)
            opportunity_score = self._calculate_opportunity_score(search_volume, competition)
            
            analyzed_keywords.append({
                'keyword': keyword,
                'monthly_volume': search_volume,
                'competition': competition,
                'opportunity_score': opportunity_score,
                'difficulty': self._get_difficulty_label(competition)
            })
        
        return analyzed_keywords
    
    def _estimate_search_volume(self, keyword):
        base_volume = 100
        keyword_lower = keyword.lower()
        
        for pattern, (min_vol, max_vol) in self.search_volume_ranges.items():
            if pattern in keyword_lower:
                base_volume = random.randint(min_vol, max_vol)
                break
        
        # Adjust based on keyword length (long-tail usually has lower volume)
        word_count = len(keyword.split())
        if word_count > 3:
            base_volume = max(10, base_volume // word_count)
        
        return base_volume
    
    def _estimate_competition(self, keyword):
        base_competition = 50
        
        # Higher competition for short, popular keywords
        word_count = len(keyword.split())
        if word_count <= 2:
            base_competition = random.randint(70, 95)
        elif word_count == 3:
            base_competition = random.randint(40, 75)
        else:  # 4+ words (long-tail)
            base_competition = random.randint(10, 50)
        
        # Higher competition for commercial intent
        commercial_terms = ['buy', 'price', 'cost', 'deal', 'discount', 'cheap', 'sale']
        if any(term in keyword.lower() for term in commercial_terms):
            base_competition = min(95, base_competition + 20)
        
        return base_competition
    
    def _calculate_opportunity_score(self, volume, competition):
        # Normalize volume (0-1 scale)
        volume_score = min(volume / 10000, 1.0)
        
        # Invert competition (lower competition = higher score)
        competition_score = 1 - (competition / 100)
        
        # Weighted combination (60% competition, 40% volume)
        opportunity_score = (volume_score * 0.4) + (competition_score * 0.6)
        
        return round(opportunity_score * 100, 2)
    
    def _get_difficulty_label(self, competition):
        if competition < 30:
            return "Very Easy"
        elif competition < 50:
            return "Easy"
        elif competition < 70:
            return "Medium"
        elif competition < 85:
            return "Hard"
        else:
            return "Very Hard"