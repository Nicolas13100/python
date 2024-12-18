using UnityEngine;
using System.Collections.Generic;

public class RandomMapGenerator : MonoBehaviour
{
    public GameObject largeSallePrefab;      // Prefab for large room
    public GameObject smallSallePrefab;      // Prefab for small room
    public GameObject horizontalCouloirPrefab; // Prefab for horizontal corridor
    public GameObject verticalCouloirPrefab;   // Prefab for vertical corridor

    public int mapWidth = 20;  // Number of columns
    public int mapHeight = 20; // Number of rows
    public float tileSize = 50.0f; // Size of each tile

    private int[,] _mapGrid; // 2D grid for map layout
    private List<Vector3> _roomPositions = new List<Vector3>(); // Room positions

    void Start()
    {
        GenerateMap();
    }

    void GenerateMap()
    {
        // Initialize the grid
        _mapGrid = new int[mapWidth, mapHeight];

        // Place the required elements
        PlaceLargeRoom();
        PlaceSmallRooms();
        PlaceHorizontalCorridors();
        PlaceVerticalCorridors();

        // Render the map based on the grid
        RenderMap();
    }

    void PlaceLargeRoom()
    {
        // Place the large room in the center of the map
        Vector3 roomSize = largeSallePrefab.GetComponent<Renderer>().bounds.size;
        int roomWidth = Mathf.CeilToInt(roomSize.x / tileSize);
        int roomHeight = Mathf.CeilToInt(roomSize.z / tileSize);

        int xPos = mapWidth / 2 - roomWidth / 2;
        int zPos = mapHeight / 2 - roomHeight / 2;

        PlaceRoom(xPos, zPos, roomWidth, roomHeight, largeSallePrefab);
    }

    void PlaceSmallRooms()
    {
        int smallRoomsPlaced = 0;
        Vector3 roomSize = smallSallePrefab.GetComponent<Renderer>().bounds.size;
        int roomWidth = Mathf.CeilToInt(roomSize.x / tileSize);
        int roomHeight = Mathf.CeilToInt(roomSize.z / tileSize);

        while (smallRoomsPlaced < 2)
        {
            int xPos = Random.Range(0, mapWidth - roomWidth);
            int zPos = Random.Range(0, mapHeight - roomHeight);

            if (!CheckRoomOverlap(xPos, zPos, roomWidth, roomHeight))
            {
                PlaceRoom(xPos, zPos, roomWidth, roomHeight, smallSallePrefab);
                smallRoomsPlaced++;
            }
        }
    }

    void PlaceHorizontalCorridors()
    {
        int corridorsPlaced = 0;

        while (corridorsPlaced < 3)
        {
            int zPos = Random.Range(0, mapHeight); // Random row
            int startX = Random.Range(0, mapWidth - 3); // Random start point
            int endX = startX + Random.Range(3, 5); // Ensure at least 3 tiles length

            if (endX < mapWidth && CheckHorizontalCorridorClear(startX, zPos, endX))
            {
                CreateHorizontalCorridor(startX, zPos, endX);
                corridorsPlaced++;
            }
        }
    }

    void PlaceVerticalCorridors()
    {
        int corridorsPlaced = 0;

        while (corridorsPlaced < 4)
        {
            int xPos = Random.Range(0, mapWidth); // Random column
            int startZ = Random.Range(0, mapHeight - 3); // Random start point
            int endZ = startZ + Random.Range(3, 5); // Ensure at least 3 tiles length

            if (endZ < mapHeight && CheckVerticalCorridorClear(xPos, startZ, endZ))
            {
                CreateVerticalCorridor(xPos, startZ, endZ);
                corridorsPlaced++;
            }
        }
    }

    void PlaceRoom(int xPos, int zPos, int roomWidth, int roomHeight, GameObject roomPrefab)
    {
        for (int x = xPos; x < xPos + roomWidth; x++)
        {
            for (int z = zPos; z < zPos + roomHeight; z++)
            {
                _mapGrid[x, z] = 1; // Mark as room
            }
        }

        Vector3 roomPosition = new Vector3(
            (xPos + roomWidth / 2.0f) * tileSize,
            0,
            (zPos + roomHeight / 2.0f) * tileSize
        );

        Instantiate(roomPrefab, roomPosition, Quaternion.identity);
        _roomPositions.Add(roomPosition);
    }

    bool CheckRoomOverlap(int xPos, int zPos, int roomWidth, int roomHeight)
    {
        for (int x = xPos; x < xPos + roomWidth; x++)
        {
            for (int z = zPos; z < zPos + roomHeight; z++)
            {
                if (x >= mapWidth || z >= mapHeight || _mapGrid[x, z] != 0)
                {
                    return true; // Overlap or out of bounds
                }
            }
        }
        return false; // No overlap
    }

    bool CheckHorizontalCorridorClear(int startX, int zPos, int endX)
    {
        for (int x = startX; x <= endX; x++)
        {
            if (_mapGrid[x, zPos] != 0) return false; // Blocked
        }
        return true;
    }

    bool CheckVerticalCorridorClear(int xPos, int startZ, int endZ)
    {
        for (int z = startZ; z <= endZ; z++)
        {
            if (_mapGrid[xPos, z] != 0) return false; // Blocked
        }
        return true;
    }

    void CreateHorizontalCorridor(int startX, int zPos, int endX)
    {
        for (int x = startX; x <= endX; x++)
        {
            _mapGrid[x, zPos] = 3; // Mark as horizontal corridor
            Instantiate(horizontalCouloirPrefab, new Vector3(x * tileSize, 0, zPos * tileSize), Quaternion.identity);
        }
    }

    void CreateVerticalCorridor(int xPos, int startZ, int endZ)
    {
        for (int z = startZ; z <= endZ; z++)
        {
            _mapGrid[xPos, z] = 4; // Mark as vertical corridor
            Instantiate(verticalCouloirPrefab, new Vector3(xPos * tileSize, 0, z * tileSize), Quaternion.identity);
        }
    }

    void ConnectRoomsWithCorridors()
    {
        // Connect each room to the next one in the list
        for (int i = 0; i < _roomPositions.Count - 1; i++)
        {
            Vector3 currentRoom = _roomPositions[i];
            Vector3 nextRoom = _roomPositions[i + 1];

            int currentRoomX = Mathf.FloorToInt(currentRoom.x / tileSize);
            int currentRoomZ = Mathf.FloorToInt(currentRoom.z / tileSize);
            int nextRoomX = Mathf.FloorToInt(nextRoom.x / tileSize);
            int nextRoomZ = Mathf.FloorToInt(nextRoom.z / tileSize);

            // Create a horizontal corridor between rooms
            CreateHorizontalCorridor(currentRoomX, currentRoomZ, nextRoomX);

            // Create a vertical corridor between rooms
            CreateVerticalCorridor(nextRoomX, currentRoomZ, nextRoomZ);
        }
    }
    
    void RenderMap()
    {
        // Render already handled during placement.
    }
}
