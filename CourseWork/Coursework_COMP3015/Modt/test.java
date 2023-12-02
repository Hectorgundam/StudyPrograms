# First, I'll create the Java entity classes for Movie, Actor, and MovieActor with the appropriate JPA annotations.
# Then, I will write these classes to files and compress them into a ZIP archive.

# Define the Java code for the three entities

movie_entity_code = """
import javax.persistence.*;
import java.util.Date;
import java.util.Set;

@Entity
@Table(name = "Movie")
public class Movie {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "Title", length = 50, nullable = false)
    private String title;

    @Column(name = "Genre", length = 25, nullable = false)
    private String genre;

    @Column(name = "ReleaseDate")
    @Temporal(TemporalType.DATE)
    private Date releaseDate;

    @ManyToMany(mappedBy = "movies")
    private Set<Actor> actors;

    // Constructors, getters, setters, and other methods are omitted for brevity
}
"""

actor_entity_code = """
import javax.persistence.*;
import java.util.Set;

@Entity
@Table(name = "Actor")
public class Actor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "FirstName", length = 45, nullable = false)
    private String firstName;

    @Column(name = "LastName", length = 45, nullable = false)
    private String lastName;

    @ManyToMany
    @JoinTable(
        name = "MovieActor",
        joinColumns = @JoinColumn(name = "ActorID"),
        inverseJoinColumns = @JoinColumn(name = "MovieID")
    )
    private Set<Movie> movies;

    // Constructors, getters, setters, and other methods are omitted for brevity
}
"""

movie_actor_entity_code = """
import javax.persistence.*;

@Entity
@Table(name = "MovieActor")
public class MovieActor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "MovieID", insertable = false, updatable = false)
    private int movieId;

    @Column(name = "ActorID", insertable = false, updatable = false)
    private int actorId;

    @ManyToOne
    @JoinColumn(name = "MovieID", referencedColumnName = "ID")
    private Movie movie;

    @ManyToOne
    @JoinColumn(name = "ActorID", referencedColumnName = "ID")
    private Actor actor;

    // Constructors, getters, setters, and other methods are omitted for brevity
}
"""

# Now, I will write these entity class codes to their respective Java files.
import zipfile
import os

# Directory for the entity files
entities_dir = "/mnt/data/entities"
os.makedirs(entities_dir, exist_ok=True)

# File paths
movie_file_path = os.path.join(entities_dir, "Movie.java")
actor_file_path = os.path.join(entities_dir, "Actor.java")
movie_actor_file_path = os.path.join(entities_dir, "MovieActor.java")

# Write the entity code to the files
with open(movie_file_path, "w") as file:
    file.write(movie_entity_code)

with open(actor_file_path, "w") as file:
    file.write(actor_entity_code)

with open(movie_actor_file_path, "w") as file:
    file.write(movie_actor_entity_code)

# Create a ZIP file containing the entity files
zip_file_path = "/mnt/data/entities.zip"
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    zipf.write(movie_file_path, os.path.basename(movie_file_path))
    zipf.write(actor_file_path, os.path.basename(actor_file_path))
    zipf.write(movie_actor_file_path, os.path.basename(movie_actor_file_path))

zip_file_path
