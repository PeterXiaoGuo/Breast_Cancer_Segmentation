'''
def dice_loss(input, target):

    iflat = input.view(-1)
    tflat = target.view(-1)
    intersection = (iflat * tflat).sum()

    return (2 * intersection) / (iflat.sum() + tflat.sum())
'''


def dice_loss(input,target):
    # target.size() -> [n, h, w] \ in {0, 1}
    print(target.size()) # [384, 384] \ in {0, 1}
    inter = (input * target).sum(-1).sum(-1)
    union = input.sum(-1).sum(-1) + target.sum(-1).sum(-1)
    result = (2 * inter / union).mean()
    print('Result: ' + str(result))
    return result
