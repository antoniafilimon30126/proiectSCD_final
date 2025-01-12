package socialmedia.server.comment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/comment")
public class CommentController {

    @Autowired
    private CommentService commentService;

    // CREATE - Creare comentariu
    @PostMapping
    public Comment createComment(@RequestBody Comment comment) {
        return commentService.createComment(comment);
    }

    // READ - Obține toate comentariile
    @GetMapping
    public List<Comment> getAllComments() {
        return commentService.getAllComments();
    }

    // READ - Obține un comentariu după ID
    @GetMapping("/{id}")
    public Comment getCommentById(@PathVariable Integer id) {
        Optional<Comment> comment = commentService.getCommentById(id);
        if (comment.isPresent()) {
            return comment.get();
        } else {
            throw new RuntimeException("Comment not found for id: " + id);
        }
    }

    // UPDATE - Actualizare comentariu
    @PutMapping("/{id}")
    public Comment updateComment(@PathVariable Integer id, @RequestBody Comment commentDetails) {
        return commentService.updateComment(id, commentDetails);
    }

    // DELETE - Șterge comentariu
    @DeleteMapping("/{id}")
    public void deleteComment(@PathVariable Integer id) {
        commentService.deleteComment(id);
    }
}
