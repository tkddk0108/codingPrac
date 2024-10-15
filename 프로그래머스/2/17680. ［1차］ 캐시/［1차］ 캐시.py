def solution(cacheSize, cities):
    answer = 0
    cache = [''] * cacheSize
    
    lower = [city.lower() for city in cities]
    
    for city in lower:
        if city in cache: #캐시히트
            cache.remove(city)
            cache.append(city)
            answer +=1 
        else: #캐시미스
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                cache.append(city)
            answer += 5 
    return answer