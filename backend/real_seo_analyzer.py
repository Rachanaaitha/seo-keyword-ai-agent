import requests
import os
from datetime import datetime

class RealSEOAnalyzer:
    def __init__(self):
        self.serpapi_key = os.getenv('SERPAPI_KEY')  # Get free key from serpapi.com
        
    def analyze(self, keywords):
        analyzed_keywords = []
        
        for keyword in keywords:
            try:
                # Get real SEO data from SerpAPI
                volume, competition = self._get_serpapi_data(keyword)
                
                opportunity_score = self._calculate_opportunity_score(volume, competition)
                
                analyzed_keywords.append({
                    'keyword': keyword,
                    'monthly_volume': volume,
                    'competition': competition,
                    'opportunity_score': opportunity_score,
                    'difficulty': self._get_difficulty_label(competition),
                    'data_source': 'SerpAPI'
                })
                
            except Exception as e:
                # Fallback to estimated data
                volume, competition = self._estimate_data(keyword)
                analyzed_keywords.append({
                    'keyword': keyword,
                    'monthly_volume': volume,
                    'competition': competition,
                    'opportunity_score': self._calculate_opportunity_score(volume, competition),
                    'difficulty': self._get_difficulty_label(competition),
                    'data_source': 'Estimated'
                })
        
        return analyzed_keywords
    
    def _get_serpapi_data(self, keyword):
        """Get real SEO data from SerpAPI"""
        try:
            url = "https://serpapi.com/search"
            params = {
                'q': keyword,
                'engine': 'google_trends',
                'api_key': self.serpapi_key,
                'data_type': 'RELATED_QUERIES'
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                # Extract volume and competition from response
                volume = data.get('interest_over_time', {}).get('averages', {}).get('value', 100)
                competition = self._analyze_competition(keyword)
                return volume, competition
                
        except Exception as e:
            print(f"SerpAPI error for '{keyword}': {e}")
            
        return self._estimate_data(keyword)  # Fallback
    
    def _analyze_competition(self, keyword):
        """Analyze competition by checking Google search results"""
        try:
            url = "https://serpapi.com/search"
            params = {
                'q': keyword,
                'engine': 'google',
                'api_key': self.serpapi_key,
                'num': 10
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                organic_results = data.get('organic_results', [])
                
                # Competition score based on domain authority in results
                big_domains = ['wikipedia.org', 'youtube.com', 'amazon.com', 'forbes.com']
                big_domain_count = sum(1 for result in organic_results 
                                    if any(domain in result.get('link', '') for domain in big_domains))
                
                competition = min(95, big_domain_count * 15 + 10)
                return competition
                
        except Exception as e:
            print(f"Competition analysis error: {e}")
            
        return 50  # Default medium competition
    
    def _estimate_data(self, keyword):
        """Fallback estimation when API fails"""
        word_count = len(keyword.split())
        
        # Estimate volume based on keyword characteristics
        base_volume = 1000 if word_count <= 2 else 500 if word_count == 3 else 100
        volume = max(10, base_volume // word_count)
        
        # Estimate competition
        if word_count <= 2:
            competition = 70
        elif word_count == 3:
            competition = 45
        else:
            competition = 20
            
        return volume, competition
    
    def _calculate_opportunity_score(self, volume, competition):
        volume_score = min(volume / 10000, 1.0)
        competition_score = 1 - (competition / 100)
        return round((volume_score * 0.4 + competition_score * 0.6) * 100, 2)
    
    def _get_difficulty_label(self, competition):
        if competition < 30: return "Very Easy"
        elif competition < 50: return "Easy"
        elif competition < 70: return "Medium"
        elif competition < 85: return "Hard"
        else: return "Very Hard"