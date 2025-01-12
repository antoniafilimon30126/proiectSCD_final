package socialmedia.server.post;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import socialmedia.server.user.User;
import socialmedia.server.comment.Comment;  // Corect importul

import java.util.Date;
import java.util.List;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Post {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private String title;

    private String content;

    @CreationTimestamp
    @Column(updatable = false, nullable = false)
    private Date createdOn;

    private Status status;

    @ManyToOne
    @JoinColumn(name="user_id", nullable = true)
    private User user;

    @OneToMany(mappedBy = "post")  // Legătura inversă cu Comment
    private List<Comment> comments;  // Lista comentariilor pentru această postare
}
