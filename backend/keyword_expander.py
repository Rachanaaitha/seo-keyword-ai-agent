import requests
import re

class KeywordExpander:
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "mistral"
        
    def expand(self, seed_keyword):
        try:
            # Check if Ollama is running
            try:
                response = requests.get("http://localhost:11434/api/tags", timeout=5)
                if response.status_code != 200:
                    print("⚠️  Ollama not running. Using mock data.")
                    return self._generate_mock_keywords(seed_keyword)
            except:
                print("⚠️  Cannot connect to Ollama. Using mock data.")
                return self._generate_mock_keywords(seed_keyword)
            
            prompt = f"""
            Generate 150 SEO keyword variations for "{seed_keyword}". Return ONLY a comma-separated list.

            Include these types:
            - Long-tail keywords (3-5 words)
            - Question-based keywords (how, what, why, when)
            - Geographic variations (cities, countries)
            - "Near me" and local keywords
            - Comparison keywords (vs, alternatives, best)
            - Price and cost related
            - Review and rating keywords
            - Beginner/friendly keywords
            - 2024/2025 trend keywords

            Example for "coffee shop": best coffee shops near me, how to start a coffee shop, coffee shop business plan, affordable coffee machines

            Now generate for: "{seed_keyword}"
            """
            
            data = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 1000
                }
            }
            
            response = requests.post(self.ollama_url, json=data, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                keywords_text = result["response"].strip()
                
                # Clean the response
                keywords_text = re.sub(r'^\d+\.\s*', '', keywords_text, flags=re.MULTILINE)
                keywords_text = re.sub(r'["\']', '', keywords_text)
                
                # Split by commas and newlines
                keywords = []
                for line in keywords_text.split('\n'):
                    for kw in line.split(','):
                        clean_kw = kw.strip()
                        if clean_kw and len(clean_kw) > 2:
                            keywords.append(clean_kw)
                
                unique_keywords = list(set(keywords))
                print(f"✅ AI generated {len(unique_keywords)} keywords")
                return unique_keywords[:100]
                
            else:
                print("❌ Ollama API error. Using mock data.")
                return self._generate_mock_keywords(seed_keyword)
                
        except Exception as e:
            print(f"❌ Error: {e}. Using mock data.")
            return self._generate_mock_keywords(seed_keyword)
    
    def _generate_mock_keywords(self, seed_keyword):
        """Generate mock keywords when Ollama is not available"""
        patterns = [
            f"best {seed_keyword}",
            f"how to {seed_keyword}",
            f"{seed_keyword} for beginners",
            f"affordable {seed_keyword}",
            f"{seed_keyword} near me",
            f"{seed_keyword} 2024",
            f"why {seed_keyword} is important",
            f"{seed_keyword} vs alternatives",
            f"free {seed_keyword}",
            f"professional {seed_keyword}",
            f"{seed_keyword} tips and tricks",
            f"{seed_keyword} best practices",
            f"how much does {seed_keyword} cost",
            f"{seed_keyword} reviews",
            f"is {seed_keyword} worth it",
            f"learn {seed_keyword} online",
            f"{seed_keyword} course",
            f"{seed_keyword} tutorial",
            f"what is {seed_keyword}",
            f"benefits of {seed_keyword}",
            f"{seed_keyword} guide",
            f"{seed_keyword} strategies",
            f"{seed_keyword} tools",
            f"{seed_keyword} software",
            f"{seed_keyword} services",
            f"top 10 {seed_keyword}",
            f"{seed_keyword} ideas",
            f"{seed_keyword} examples",
            f"{seed_keyword} techniques",
            f"{seed_keyword} for small business"
        ]
        
        # Add geographic variations
        cities = ["new york", "london", "tokyo", "dubai", "sydney", "paris", "berlin"]
        for city in cities:
            patterns.extend([
                f"{seed_keyword} in {city}",
                f"best {seed_keyword} {city}",
                f"{city} {seed_keyword} services",
                f"{seed_keyword} near {city}"
            ])
        
        return list(set(patterns))[:80]