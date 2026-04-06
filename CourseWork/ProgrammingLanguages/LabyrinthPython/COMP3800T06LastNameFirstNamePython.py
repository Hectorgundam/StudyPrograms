import os

def get_full_path(filename):
    script_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_folder, filename)

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt)

        if len(user_input) == 0:
            continue

        c = user_input[0]

        if c == "S" or c == "s":
            return True
        if c == "N" or c == "n":
            return False

        print("Invalid input. Enter S or N.")


def print_line_to_screen_and_file(text, out_file):
    print(text)

    if out_file is not None:
        out_file.write(text + "\n")


def print_grid_to_screen_and_file(grid, rows, out_file):
    for r in range(rows):
        print_line_to_screen_and_file(grid[r], out_file)



def read_maze_file():
    user_input = input("Enter maze file name: ").strip()

    if len(user_input) >= 4 and user_input[-4:] == ".txt":
        filename = user_input
    else:
        filename = user_input + ".txt"

    full_path = get_full_path(filename)

    maze = []

    try:
        file = open(full_path, "r")
    except:
        print("Could not open file:", filename)
        print("Looking in:", full_path)
        return [], 0, 0, False

    cols = -1

    for line in file:
        line = line.rstrip("\n")

        if cols == -1:
            cols = len(line)

        if len(line) != cols:
            print("Error: maze must be rectangular.")
            file.close()
            return [], 0, 0, False

        maze.append(line)

    file.close()

    rows = len(maze)

    if rows == 0:
        print("Error: file is empty.")
        return [], 0, 0, False

    return maze, rows, cols, True


def validate_maze_size(rows, cols):
    if rows < 8 or cols < 8:
        print("Error: maze must be at least 8 rows and 8 columns.")
        return False

    if rows > 64 or cols > 64:
        print("Error: maze cannot exceed 64 rows or 64 columns.")
        return False

    return True


def find_start_and_exit(maze, rows, cols):
    start_r = -1
    start_c = -1
    end_r = -1
    end_c = -1

    start_count = 0
    end_count = 0

    for r in range(rows):
        for c in range(cols):
            ch = maze[r][c]

            if ch == "*":
                start_count += 1
                start_r = r
                start_c = c

            if ch == "+":
                end_count += 1
                end_r = r
                end_c = c

    if start_count != 1:
        print("Error: maze must contain exactly one start point (*).")
        return -1, -1, -1, -1, False

    if end_count != 1:
        print("Error: maze must contain exactly one exit point (+).")
        return -1, -1, -1, -1, False

    return start_r, start_c, end_r, end_c, True


def step_dir_name(from_r, from_c, to_r, to_c):
    if to_r == from_r and to_c == from_c + 1:
        return "right"
    if to_r == from_r and to_c == from_c - 1:
        return "left"
    if to_r == from_r - 1 and to_c == from_c:
        return "up"
    return "down"


def is_walkable(cell):
    if cell == "." or cell == " " or cell == "*" or cell == "+":
        return True
    return False


def solve_maze(original, rows, cols, show_process, out_file):
    work = []
    for r in range(rows):
        work.append(original[r])

    start_r, start_c, end_r, end_c, found_points = find_start_and_exit(original, rows, cols)

    if not found_points:
        return [], [], False

    visited = []
    for r in range(rows):
        visited_row = []
        for c in range(cols):
            visited_row.append(False)
        visited.append(visited_row)

    path_r = []
    path_c = []

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    path_r.append(start_r)
    path_c.append(start_c)
    visited[start_r][start_c] = True

    total_moves = 0

    if show_process:
        print_line_to_screen_and_file("", out_file)
        print_line_to_screen_and_file("Solution Process:", out_file)
        print_line_to_screen_and_file(
            "The user entered the maze at (" + str(start_r) + "," + str(start_c) + ").",
            out_file
        )

    while len(path_r) > 0:
        cur_r = path_r[len(path_r) - 1]
        cur_c = path_c[len(path_c) - 1]

        if cur_r == end_r and cur_c == end_c:
            solved = []
            for r in range(rows):
                solved.append(original[r])

            for i in range(len(path_r)):
                rr = path_r[i]
                cc = path_c[i]

                row_as_list = list(solved[rr])

                if row_as_list[cc] != "*" and row_as_list[cc] != "+":
                    row_as_list[cc] = "o"

                solved[rr] = "".join(row_as_list)

            if show_process:
                print_line_to_screen_and_file(
                    "The user reached the exit at (" + str(end_r) + "," + str(end_c) + ") after " +
                    str(total_moves) + " step" + ("" if total_moves == 1 else "s") + ".",
                    out_file
                )

            path = []
            for i in range(len(path_r)):
                path.append((path_r[i], path_c[i]))

            return solved, path, True

        moved = False

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            cell = work[nr][nc]

            if not is_walkable(cell):
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            path_r.append(nr)
            path_c.append(nc)
            total_moves += 1
            moved = True

            if show_process:
                direction = step_dir_name(cur_r, cur_c, nr, nc)
                print_line_to_screen_and_file(
                    "Move " + direction + " to (" + str(nr) + "," + str(nc) + ").",
                    out_file
                )

            break

        if moved:
            continue

        if show_process:
            print_line_to_screen_and_file(
                "Dead end at (" + str(cur_r) + "," + str(cur_c) + "). Backtracking.",
                out_file
            )

        if work[cur_r][cur_c] != "*" and work[cur_r][cur_c] != "+":
            row_as_list = list(work[cur_r])
            row_as_list[cur_c] = "#"
            work[cur_r] = "".join(row_as_list)

        path_r.pop()
        path_c.pop()

    return [], [], False


def grid_to_vrml_coords(row, col, maze_width, maze_height):
    x = col - (maze_width / 2.0) + 0.5
    z = row - (maze_height / 2.0) + 0.5
    y = 0
    return x, y, z


def build_vrml_header():
    text = ""
    text += "#VRML V2.0 utf8\n\n"
    text += "NavigationInfo {\n"
    text += "  avatarSize [0.25, 2, 0.75]\n"
    text += "}\n\n"
    return text


def build_floor(maze_width, maze_height, wall_height, floor_texture):
    floor_y = -(wall_height / 2.0)

    text = ""
    text += "DEF Floor Transform {\n"
    text += "  translation 0 " + str(floor_y) + " 0\n"
    text += "  children [\n"
    text += "    Shape {\n"
    text += "      appearance Appearance {\n"
    text += "        texture ImageTexture { url [\"" + floor_texture + "\"] }\n"
    text += "      }\n"
    text += "      geometry Box {\n"
    text += "        size " + str(maze_width) + " 0.1 " + str(maze_height) + "\n"
    text += "      }\n"
    text += "    }\n"
    text += "  ]\n"
    text += "}\n\n"

    return text


def build_box(x, y, z, wall_height, wall_texture, index):
    text = ""
    text += "DEF Box" + str(index) + " Transform {\n"
    text += "  translation " + str(x) + " " + str(y) + " " + str(z) + "\n"
    text += "  children [\n"
    text += "    Shape {\n"
    text += "      appearance Appearance {\n"
    text += "        texture ImageTexture { url [\"" + wall_texture + "\"] }\n"
    text += "      }\n"
    text += "      geometry Box {\n"
    text += "        size 1 " + str(wall_height) + " 1\n"
    text += "      }\n"
    text += "    }\n"
    text += "  ]\n"
    text += "}\n\n"
    return text


def build_cone(x, y, z, wall_height, wall_texture, index):
    text = ""
    text += "DEF Cone" + str(index) + " Transform {\n"
    text += "  translation " + str(x) + " " + str(y) + " " + str(z) + "\n"
    text += "  children [\n"
    text += "    Shape {\n"
    text += "      appearance Appearance {\n"
    text += "        texture ImageTexture { url [\"" + wall_texture + "\"] }\n"
    text += "      }\n"
    text += "      geometry Cone {\n"
    text += "        height " + str(wall_height) + "\n"
    text += "        bottomRadius 0.5\n"
    text += "        side TRUE\n"
    text += "        bottom TRUE\n"
    text += "      }\n"
    text += "    }\n"
    text += "  ]\n"
    text += "}\n\n"
    return text


def build_solution_tile(x, z, tile_index, wall_height):
    floor_y = -(wall_height / 2.0)
    tile_y = floor_y + 0.1

    text = ""
    text += "DEF PathTile" + str(tile_index) + " Transform {\n"
    text += "  translation " + str(x) + " " + str(tile_y) + " " + str(z) + "\n"
    text += "  children [\n"
    text += "    Shape {\n"
    text += "      appearance Appearance {\n"
    text += "        material Material {\n"
    text += "          diffuseColor 1 1 0\n"
    text += "        }\n"
    text += "      }\n"
    text += "      geometry Box {\n"
    text += "        size 0.8 0.1 0.8\n"
    text += "      }\n"
    text += "    }\n"
    text += "  ]\n"
    text += "}\n\n"
    return text


def build_maze_objects(maze, rows, cols, wall_height, wall_texture):
    text = ""
    box_index = 1
    cone_index = 1

    for row in range(rows):
        for col in range(cols):
            ch = maze[row][col]
            x, y, z = grid_to_vrml_coords(row, col, cols, rows)

            if ch == "B":
                text += build_box(x, 0, z, wall_height, wall_texture, box_index)
                box_index += 1
            elif ch == "C":
                text += build_cone(x, 0, z, wall_height, wall_texture, cone_index)
                cone_index += 1

    return text


def build_solution_path(path, rows, cols, wall_height):
    text = ""
    tile_index = 1

    for position in path:
        row = position[0]
        col = position[1]
        x, y, z = grid_to_vrml_coords(row, col, cols, rows)
        text += build_solution_tile(x, z, tile_index, wall_height)
        tile_index += 1

    return text


def write_vrml_file(filename, content):
    full_path = get_full_path(filename)

    try:
        file = open(full_path, "w")
        file.write(content)
        file.close()
        print("VRML file created successfully:", filename)
        print("Saved in:", full_path)
    except:
        print("Error: Could not write VRML file.")
        print("Tried to save in:", full_path)


def main():
    maze, rows, cols, ok = read_maze_file()

    if not ok:
        print("Failed to read maze.")
        return

    if not validate_maze_size(rows, cols):
        print("Maze size validation failed.")
        return

    print("\nMaze loaded successfully.")
    print("Rows:", rows, " Cols:", cols)
    print()

    show_process = get_yes_no_input("Show solution process on screen? (S or N): ")
    print()

    wall_height = float(input("Enter wall height in meters: "))
    wall_texture = input("Enter wall texture file name: ").strip()
    floor_texture = input("Enter floor texture file name: ").strip()
    output_vrml = input("Enter output VRML file name: ").strip()

    if len(output_vrml) < 4 or output_vrml[-4:] != ".wrl":
        output_vrml += ".wrl"

    solved, path, success = solve_maze(maze, rows, cols, show_process, None)

    if not success:
        print("No solution found.")
        return

    print()
    print("Solution:")
    print()

    print_grid_to_screen_and_file(solved, rows, None)

    vrml_text = ""
    vrml_text += build_vrml_header()
    vrml_text += build_floor(cols, rows, wall_height, floor_texture)
    vrml_text += build_maze_objects(maze, rows, cols, wall_height, wall_texture)
    vrml_text += build_solution_path(path, rows, cols, wall_height)

    write_vrml_file(output_vrml, vrml_text)


main()