import numpy as np

def xbuckets( tvecs ) :
    xmin = np.amin(tvecs[:,0])
    xmax = np.amax(tvecs[:,0])
    xrange = xmax - xmin
    step = xrange/3
    b1 = np.array([0,step])
    b2 = np.array([step,2*step])
    b3 = np.array([2*step,xrange])

    return [b1, b2, b3]

def sortxy( tvecs ) :
    print(tvecs)
    tvecs = tvecs[tvecs[:,0].argsort()]
    print(tvecs)
    tvecs = tvecs[tvecs[:,1].argsort()]
    print(tvecs)
    return tvecs

def random_tvecs() :
    return np.random.rand(10,3)

def layering( tvecs, epsilon ) :
    length = tvecs.shape[0]
    layers = []
    i=0
    while i < length :
        print(i)
        y1 = tvecs[i, 1]
        y1_block = tvecs[i, :]
        error = [y1-epsilon, y1+epsilon]
        layer = [y1_block]
        if i+1 >= length :
            pass
        elif i+2 >= length :
            y2 = tvecs[i+1, 1]
            y2_block = tvecs[i+1, :]
            avg = (y1+y2)/2
            if avg >= error[0] and avg <= error[1] :
                layer += [y2_block]
            #layer could equal yi or yi + yi1
        elif i+2 < length :
            y2 = tvecs[i+1, 1]
            y2_block = tvecs[i+1, :]
            y3 = tvecs[i+2, 1]
            y3_block = tvecs[i+2, :]
            avg1 = (y1+y2+y3)/3
            avg2 = (y1+y2)/2
            if avg1 >= error[0] and avg1 <= error[1] :
                layer += [y2_block]
                layer += [y3_block]
                #layer = layer.append(y3)
                i += 2
            elif avg2 >= error[0] and avg2 <= error[1] :
                layer += [y2_block]
                i += 1
            #layer could equal i, i1, i12
        layers += [layer]
        i+=1
    return layers

def pick_block( tvecs, epsilon ) :
    #sorts by x then y
    tvecs = sortxy(tvecs)
    #plops block into respective layers within a tolerance of epsilon
    layers = layering(a, epsilon)
    #removes top 3 layers as they aren't legal to pull from
    del layers[-3:]
    #first check for a full layer
    for layer in layers :
        if len(layer) == 3 :
            #returns middle block of layer if layer is full (this is best case)
            return layer[1]
        #if layer has one block, immediately remove it from consideration
        elif len(layer) == 1 :
            layers.remove(layer)
    #in worst case, there are no 3 block
    for layer in layers

#a = random_tvecs()
if __name__ == "__main__" :
    a = np.array([[1, 1, 0],
                  [3, 1, 0],
                  [5, 1, 0],
                  [1, 2, 0],
                  [3, 2, 0],
                  [1, 3, 0],
                  [5, 3, 0],
                  [1, 4, 0],
                  [1, 5, 0],
                  [3, 5, 0],
                  [5, 5, 0]])
    block = pick_block(a, .05)
    print(block)
    #for layer in layers :
    #    print(layer)
