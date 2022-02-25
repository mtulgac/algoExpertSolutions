def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(1,len(redShirtHeights)):
            if redShirtHeights[i] < blueShirtHeights[i]:
                continue
            else:
                return False
    elif redShirtHeights[0] > blueShirtHeights[0]:
        for i in range(1,len(redShirtHeights)):
            if blueShirtHeights[i] < redShirtHeights[i]:
                continue
            else:
                return False	
    else:
        return False		
    return True
