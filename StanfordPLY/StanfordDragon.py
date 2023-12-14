from array import array
from OpenGL import GL
import ctypes


class StanfordDragon:
    def __init__(self):
        scale = 20
        state = 0
        vertexCount = 0
        faceCount = 0
        vertices = array("f")
        indices = array("I")

        with open("objs/dragon_vrip_res4.ply", "r") as f:
            for line in f:
                parts = line.split()
                if state == 0:
                    if len(parts) > 0 and parts[0] == "end_header":
                        state = 1
                    else:
                        if len(parts) == 3 and parts[0] == "element":
                            if parts[1] == "vertex":
                                vertexCount = int(parts[2])
                            elif parts[1] == "face":
                                faceCount = int(parts[2])
                elif state == 1:
                    vertices.append(float(parts[0]) * scale)
                    vertices.append(float(parts[1]) * scale)
                    vertices.append(float(parts[2]) * scale)
                    vertexCount -= 1
                    if vertexCount == 0:
                        state = 2
                else:
                    faceVertexCount = int(parts[0])
                    for i in range(1, faceVertexCount + 1):
                        indices.append(int(parts[i]))
                    faceCount -= 1
                    if faceCount == 0:
                        break

        self.arrayBufferId = GL.glGenVertexArrays(1)
        self.N = len(indices)
        GL.glBindVertexArray(self.arrayBufferId)
        GL.glEnableVertexAttribArray(0)

        idBuffer = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idBuffer)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, len(vertices) * vertices.itemsize,
                        ctypes.c_void_p(vertices.buffer_info()[0]), GL.GL_STATIC_DRAW)

        GL.glVertexAttribPointer(
            0, 3, GL.GL_FLOAT, GL.GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))

        idIndex = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, idIndex)
        GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, len(indices) * indices.itemsize,
                        ctypes.c_void_p(indices.buffer_info()[0]), GL.GL_STATIC_DRAW)

    def draw(self):
        GL.glBindVertexArray(self.arrayBufferId)
        GL.glDrawElements(GL.GL_TRIANGLES, self.N,
                          GL.GL_UNSIGNED_INT, ctypes.c_void_p(0))
