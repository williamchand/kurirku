"""Initialize DB

Revision ID: 02420b050291
Revises: d4867f3a4c0a
Create Date: 2021-08-14 07:52:31.090623

"""
from alembic import op
import sqlalchemy as sa
from app.core.security import get_password_hash

# revision identifiers, used by Alembic.
revision = '02420b050291'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "resi",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("tracking_name", sa.String(), nullable=True),
        sa.Column("driver_id", sa.Integer(), nullable=True),
        sa.Column("redirect_url", sa.String(), nullable=True),
        sa.Column("maps_url", sa.String(), nullable=True),
        sa.Column("sending_address", sa.String(), nullable=True),
        sa.Column("receiving_address", sa.String(), nullable=True),
        sa.Column("sending_country", sa.String(), nullable=True),
        sa.Column("receiving_country", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["driver_id"], ["user.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_resi_tracking_name"), "resi", ["tracking_name"], unique=True)
    op.create_table(
        "user_resi",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("resi_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
        sa.ForeignKeyConstraint(["resi_id"], ["resi.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "status_resi",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_resi_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_resi_id", sa.Integer(), nullable=False),
        sa.Column("status_id", sa.Integer(), nullable=False),
        sa.Column("created_timestamp", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_resi_id"], ["user_resi.id"],),
        sa.ForeignKeyConstraint(["status_id"], ["status_resi.id"],),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "user_photo",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("photo", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create an ad-hoc table to use for the insert statement.
    status_table = sa.table('status_resi',
        sa.column('id', sa.Integer),
        sa.column('status', sa.String),
    )
    op.bulk_insert(status_table,
        [
            {'id':1, 'status':'REQUESTED'},
            {'id':2, 'status':'PICKED_UP'},
            {'id':3, 'status':'IN_TRANSIT'},
            {'id':4, 'status':'DELIVERED'}
        ]
    )
    
    # Create an ad-hoc table to use for the insert statement.
    user_table = sa.table('user',
        sa.column('id', sa.Integer),
        sa.column('full_name', sa.String),
        sa.column('email', sa.String),
        sa.column('hashed_password', sa.String),
        sa.column('is_active', sa.Boolean),
        sa.column('is_superuser', sa.Boolean),
    )
    op.bulk_insert(user_table,
        [
            {'id':100, 'full_name':'Bernard Corrie', 'email': 'bernard.cor@gmail.com', 'hashed_password': get_password_hash('secret'), 'is_active': True, 'is_superuser': True },
            {'id':101, 'full_name':'Priandi Poerot', 'email': 'priandi.poe@gmail.com', 'hashed_password': get_password_hash('secret'), 'is_active': True, 'is_superuser': True },
        ]
    )
    # Create an ad-hoc table to use for the insert statement.
    resi_table = sa.table('resi',
        sa.column("id", sa.Integer),
        sa.column("tracking_name", sa.String),
        sa.column("driver_id", sa.Integer),
        sa.column("redirect_url", sa.String),
        sa.column("maps_url", sa.String),
        sa.column("sending_address", sa.String),
        sa.column("receiving_address", sa.String),
        sa.column("sending_country", sa.String),
        sa.column("receiving_country", sa.String),
    )
    op.bulk_insert(resi_table,
        [
            {
                'id':1, 
                'tracking_name':'#1234567890121', 
                'driver_id': 100, 
                'redirect_url': 'https://tlkm.me/Rs0UE3',
                'maps_url': 'https://www.google.com/maps/dir/BEC+Bandung,+Babakan+Ciamis,+Kota+Bandung,+Jawa+Barat/-6.214259,106.825661/@-6.5687514,106.6706491,9z/data=!3m1!4b1!4m8!4m7!1m5!1m1!1s0x2e68e638014b2fb5:0xa4b89c31bfb434a!2m2!1d107.609327!2d-6.907893!1m0?hl=id', 
                'sending_address': 'BEC Bandung, Babakan Ciamis, Kec. Sumur Bandung, Kota Bandung, Jawa Barat', 
                'receiving_address': 'Jakarta Selatan, Kuningan, Karet, Kecamatan Setiabudi, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12920', 
                'sending_country': 'Bandung',
                'receiving_country': 'Jakarta Selatan'
            },
            {
                'id':2, 
                'tracking_name':'#1234567890122', 
                'driver_id': 100, 
                'redirect_url': 'https://tlkm.me/3xsPiF',
                'maps_url': 'https://www.google.com/maps/dir/Jakarta+Hospital,+Jalan+Jendral+Sudirman,+RT.5%2FRW.4,+Karet+Semanggi,+South+Jakarta+City,+Jakarta/Pekanbaru+Mall,+Jalan+Jendral+Sudirman,+Rintis,+Pekanbaru+City,+Riau/@-2.8378113,99.6162959,6z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x2e69f15540a7c829:0xb9a495e45c494715!2m2!1d106.8161788!2d-6.2182371!1m5!1m1!1s0x31d5adbf53510149:0xf41bf35bbb0463a!2m2!1d101.4479579!2d0.5319514?hl=id', 
                'sending_address': 'Rumah Sakit Jakarta, Jl. Jend. Sudirman No.Kav 49, RT.5/RW.4, Karet Semanggi, Kecamatan Setiabudi, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12930', 
                'receiving_address': 'Mall Pekanbaru, Jl. Jend. Sudirman No.61, Rintis, Kec. Lima Puluh, Kota Pekanbaru, Riau 28155', 
                'sending_country': 'Jakarta Selatan',
                'receiving_country': 'Pekanbaru',
            },
            {
                'id':3, 
                'tracking_name':'#1234567890123', 
                'driver_id': 101, 
                'redirect_url': 'https://tlkm.me/XzzS38',
                'maps_url': 'https://www.google.com/maps/dir/Mall+JAMTOS+Jambi+Town+Square,+Jalan+Kapt.+A.+Bakaruddin,+Simpang+III+Sipin,+Kota+Jambi,+Jambi/OB+Fitness+%26+Health+-+Moro+Purwokerto,+Kongsen,+Purwokerto+Kulon,+Kabupaten+Banyumas,+DKI+Jakarta/@-4.5109604,101.8662042,6z/data=!4m14!4m13!1m5!1m1!1s0x2e25887ce03fd26d:0x2f89f677b808cf39!2m2!1d103.5871484!2d-1.6214759!1m5!1m1!1s0x2e655e8677089787:0x1a4f76d8d5be4183!2m2!1d109.2416449!2d-7.4288938!5i1?hl=id', 
                'sending_address': 'Jamtos, Jl. Kapt. A. Bakaruddin No.88, Simpang III Sipin, Kec. Kota Baru, Kota Jambi, Jambi 36125', 
                'receiving_address': 'OB Fitness & Health - Moro Purwokerto, Moro Purwokerto Mall Jl. Perintis Kemerdekaan No. 7, Purwokerto Selatan Banyumas, Jawa Tengah Kongsen, Kongsen, Purwokerto Kulon, Kec. Purwokerto Sel., Kabupaten Banyumas, DKI Jakarta 53141', 
                'sending_country': 'Jambi',
                'receiving_country': 'Purwokerto'
            },
            {
                'id':4, 
                'tracking_name':'#1234567890124', 
                'driver_id': 101, 
                'redirect_url': 'https://tlkm.me/yeTiIH',
                'maps_url': 'https://www.google.com/maps/dir/Pontianak+Mall,+Jl.+Teuku+Umar,+Darat+Sekip,+Kec.+Pontianak+Kota,+Kota+Pontianak,+Kalimantan+Barat+78243/Monumen+Kapal+Selam,+Jalan+Pemuda,+Embong+Kaliasin,+Surabaya,+Jawa+Timur/@-3.5905815,106.5274174,6z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x2e1d5854111fd46d:0x3786f44dd7e8543!2m2!1d109.3356708!2d-0.0315003!1m5!1m1!1s0x2dd7f9628df520e5:0x577443720136fb0b!2m2!1d112.7502656!2d-7.2657627?hl=id', 
                'sending_address': 'Pontianak Mall, Jl. Teuku Umar, Darat Sekip, Kec. Pontianak Kota, Kota Pontianak, Kalimantan Barat 78243', 
                'receiving_address': 'Monumen Kapal Selam Surabaya, Jl. Pemuda No.39, Embong Kaliasin, Kec. Genteng, Kota SBY, Jawa Timur 60271', 
                'sending_country': 'Pontianak',
                'receiving_country': 'Surabaya'
            },
        ]
    )
    
    user_photo_table = sa.table('user_photo',
        sa.column("id", sa.Integer),
        sa.column("user_id", sa.Integer),
        sa.column("photo", sa.String),
    )
    op.bulk_insert(user_photo_table,
        [
            {
                'id':1, 
                'user_id': 100, 
                'photo': '/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEBIQEBISFRUVFRUQEBAQFQ8VEBAQFRUWFhUVFRUYHSggGB0lGxUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGhAQGi0fHx0tLS0tLS0tLS0tKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKy0tLS0tLS0tLS0tLS0tLf/AABEIALcBEwMBIgACEQEDEQH/xAAcAAAABwEBAAAAAAAAAAAAAAAAAgMEBQYHAQj/xABHEAABAwIEAwUFBAcECQUAAAABAAIDBBEFEiExBkFREyJhcYEyQpGhsRRSwdEHFSNicrLhFlOCkiQzQ0STo8LS8FRjc4Oi/8QAGgEAAgMBAQAAAAAAAAAAAAAAAgMAAQQFBv/EADYRAAICAQIDBQcEAQMFAAAAAAABAhEDEiEEMUETIlGRoRRhcYHB0fAyUrHhQgUj0hWCkuLx/9oADAMBAAIRAxEAPwDDUtAy5SQCkKOLS6GbpB442yQwyEZgtGwSrDIiCdz8lnlA7vhXNmHufG0C+qyq9Wo60UnDT4jjHOHXTtDo+ZzeamOA+GJI5A6QaDZTuDsyRsYd7AK3UgAAst+LlbOXxDSlSHEMI58kuHpNzrJJ0iKrCh+lD1siUBUYJk8hehcaJQ5C7lSYejdogBaZ0tRSF3OuZ1ZNzmVDKiOkXWPurLZ3KuZUqECFLBErLlkoQutiupZNkI2XcqO5llyyuyCkMItcolTEBqEGSEIsji7dUrsGnYgilK5ULI9RYlZcLUsGrpYr1FpDYtSTmpy5iSc1EmU0N3NSbmJw4JGZ4aNUYNiD2pniI/Zu8kt9vYTa4TXFJB2ZPgjit9wGyiAfU/VdTJ2KNBI6E/VBb9Jm1GT08VypONmi5T09lK4fSZnAFealLU9jr44aUR0D8r2k9Vq/C8zHx5rjQKjY1g5aAQE1wnFHwgsB0KJNQbTGW3H4mn4ZWmSoIGzTYK+UKzXggX7x3Oq0yi2ACfifdtmbif1Uh+ACkJoUfK5u6Sla47I9VdQoQ2QgWpRsxCTZG6+qdMg6q9aClET7YlEbK66fMgCUEA6KOa8AE6CRnRdSzYl0xJesrUhs4JSJFlFknHJqg1jKtD0LtkSNyVsisQ9giUY7RELUA1Qp0CQ3RVx5XAVaYSR2yKQjojlZAqCKuoirOlczJKWRGpo7jMTvtZU6StksOQiuauSHKbeoRgVE+oTG7mKIx3SM+SsBCgOJTaN3knY3ckJnsZaWTB5dndv6KyR4iXQEO3AsUgx7bbhNKt4sbH4LpZHZnhZU56XvHzXFIadUEeoXpKtFEpnBoO+EzijU1g7O+F41SdnpYw2LDxDQg09wOSzIx2f6rbKmmz0xH7qxmubllcOhK15YtPV4mfHK414GjcDO0AWoYMy5PgFkPAtRqAtWwqpDXjxFitGNXCkZs7qVk/JGCiCEJOasa0XJAXIKtrtikSdAKM0rA6DVH7NB0w6oweEMZbl3IK0JVoTeScBdbUjqm9oiOLe46CLIU1dXNHNN34gDoLIJZUiRwzfQNOSu07Eg+dKQVIukrLvuPcXpJFjEYpNkosm1XVgDRP7RJWZ4xcnQ57YI3aBV6auSlNX35oFnRofCtKyXkKMxqZCqF09hmBCbHImKlGUUGLUVzUrdI1EoATNVC1bC5UV6Rhqw7Ygo8j1NYxwadMaVR0TOlxYx3Y5pcNxbQhK1U3VQ804Uc01TNMOGtEq/EC999hsB4KSp3XVXikBcrJhTgr7RVSAzYNCtjwtVW46flppHDkCVbJzYKj/pDn/0WQDmEeGffXxEwhqT+DMqp8Vc4lKfbHX1UVTaFPmaldrLyObie4SSY3KCTlb3igqBCUkgcrBg8feCzqgxAtOqv3C+Itc4arys+GcZWuR6LFxEZKnzNMp2/sSPBYbxCbVUgH3luDpQIC7wWE1kvaVMjurj9VtnG4owxlUmXbgOM5gtBpqvv26KicO1LIInPcQLBKcHY725eb+8fhfRacEEjJxU7LlxHI5rL3OU6eRUJw9xBKx3Z+0L2DTv6FWOWITQujPMaHoeSzuAvgqm9Wu7w62TZQjKDTVkxZmmqZqhnkNtvL+qUbiVhqqti3HVFTMu+XM+1xCwEyX6HkPUrNsZ/SlM+4p2NjB993ff6D2R8CuVj4ad21S9+39nVWfDXe3+H5XqbLU4pc2HqVHVHE0MYIdNG0jkXsv8Lrz1iGPVExJlmkdfkXG3w2CjTKeqf2OPq38lX8/YB8dW0ca+b+iX1N1qeMGZtJmnxzBS2GY5E8XE8ZPQPZf4Lzp2h6ozZyOaaoYX4+n2A9vy/tXr/Z6DxjiB7PZKgWccyNOwKyqkxuVmgebfdOrfgVLUmMRv0kGQ/ebct9W7j0+Cd2GGSpJP0f1A9tnfh6r8+RrmH8fXFsh9ShX8X3G1lSKCIWDgQ5p2c03afX8E8mguNAUC4TGv8R0M7/VsTkPEZforLhkpIuVnWHxFjr/VXChxcAWLUL4SPNI0LjLj3mTtVOQNCjYdjPIlV/EsaFjooSnxnv8AgqXCPnQL4rE1pkzW2V4te6pfGvGAiBjYe8efIJKPH2luUAk+Cq+N4c6V+c6BFHh3q7wlyhBXDdkdhHGE1M4m5c0m5aTzPRXnCuPo5u7q0+KzSswqx3KLRUeR4dcp8+HjJ3QiOfJHZq17zVqzFszTlN1Va3GX3tdPsOezstTyULisbb6FHHh4IOXET6EthuMkOF1cMOxxttVlFrOGqmqSW43VS4OMtwfbbVNGjVfEDGj2lQOL+IGytLWkqJxWpIBs4/FV101zvdXi4SMZpisvF1BxiqsMCnED9U2MaNEzXdb8nI50HQvIdSgudmglWyyihSGGVjo3AtKZ0pBKeyNAsQuKrN9o0pnFWaiLb96xHyWZCoLHF1rndStHLcWK6+JpIFk1RtWC5b0QtVjEsndJs3oFNcCV/Z1AbfR31TarwZpF27ppSwvika+3sm58kyMZKSfMTKnFo3f9cRwRmaZ4YxupcfoOp8Fk3GnG32mZxpmGNlsuc/6x9uZt7KgMdx6WpcM57rdGMHst/r4pjQ0Uk0jYomlz3nK1o5n8FeTLTqIOLHSuQg6Qk3JT2lwieQAiNwaRcOcC1pHUE7+i3Tgj9G9HRxtnrA2eo9rvi8EZ5BrTo4j7x+ATXiysilnJBADGhmum1/zSoQlOdMbarYyKLAbe24+TfzKXbg7B7t/MlWXEcRp2cwfooGr4ij9wX8k58Pp5tL4ldoum5NUnAMskYl7ONoIzNa42cRy8vVR0XDLHP7MtDXXykudla0je5JsFE1XEkj/aLj/E5x+qZnF3nl8yqisaT1TT/wC17eZep9I+qLHjPAxibniqIJOrGSNc4fQkehVTqKZ8Rs9pHQ8j5HmpiOmqy3MInAdCQ13P3Sb8uiUpMPqJpBA6Mge05z7ljW9b7E+A5qRxRUd5tvx0tLy5eRJScpd2Fe67EeG8QnbKGwAvze1Fa7Xj94ch+9pbqFqEUrLDM1wuAXMzNOQ8xmF83mo/CsNjp48kLbX9t59uQj7x/DZPAzqlZOInGFRe/j+fY14eGTfe39wrV0dh2kRzstmd9+O2+YdB94aeSksMpmuaC43vtrpZMsPqXwyCRuU2v3XC7SCLEEeSmOHJqeI/aJ3dlDE9rTnzGJpkJ7PW2gDhbW+41S/apSSiv1X5+8Y8Kxtye8UvJ9EExPApA2+R2X7xadPNVZ2Flrt9LrcqPEIJ2ZoZYpW23iex7behWO8VYnHHUPYwi2/QAp2LPUtMheKEMqba5EhhdO1o/FJ4zXsjaRcEnSw1KrLuIyBYEW8woipxMPO/zVy4lazZHhU43FkhUVwcdkg6fwUe6qCIawIlxW9l+yWqZLQ4k5ugKRlrS46qOE99kcvsj9pbXIT7PC6ss+F4eZGhxcBfbS9/EoS0zo3OaTt8LWvom2DY01rA15Iyi217jkhXYsJHlw2sAOtgg4fPllOWrkM/1PBw0cEHia1bdfO/DcjcUnvoo+NttUtVPzFFy6LX2m9nGUE+YO0XYHc02cwp62OzL+CN5L2FuNHe1QTJsgsgrpgWioseRsnLKi+hTRdauObCWiqcqdUtSHO3UK0pxTixBRrJWxWiy4RRDRExSNpjKaUdTpYlPHMa4arZHNGjP2U7KPPHZxA66LQ+FpafDou0mdmqHj2GDM6Jp2Zpz6/BQklA0a+oOlwU1kpHkHvajVrhp6FKxxjF3YycXJUXCu/SbVOaY6eHKNs0gN7eRsFSauaeQl0koGY3dY3N/TT5pKpDtCb66ka6OHMdP6pDtXbEk+BRucV1fy2Kjj931OzUI0/aG/MuGlvS6lqfh+CwzSyOJ5sDWt9L3v8AJQ4Kf4ZMR3DsdR4HmFi4lrTePZnR4BQeTTljd8vj/fIUquGHlzRTXeLHMHljS3pqbXBv8lK4Bw7LSTx1UuRwjJJiYS55BaWk7WBF7jfUJSgqsrw6/gfI9VYHT9SsceM0LdW0dDP/AKbjUu7sn6EVR17XPETY7udsBmdmHIjKdeewUrRudG6QMiL9ezc9oa+OE3aSHOF8jrW3IOvioupxN9O8uhcQybuTMbl1OuocdRcXBsQmkWJO7ZozA+AJcQADpctHVdL/AKrny4m3W6fQ43sGLFlUd9mupbDKBv6o0c490KGFaHeae00o5ridtklzO7pguQ+EjuQ+KPLWt7KSCcXilGWVjdyL3BHRwIBB6gJGSqAboqbX46DK6NpuQbE8r63V49blcW9uoORwUamlv0ILFmPpKqWEPuY3ENlZdhew6sd4XaQbeKNHxDIfbdm6iQB1/U6qS/SWWOq4pma9rTxPc4e85hdCT/ygqeu12006bv4nAUV02LE2vgd7cI84nFvyTunbRHczN+f0VURg8jmVayx6xRdzXJ/noXiPCaJ/s1DvImyO7hWM+xPf1VIbO7qlY61w2JHkSExTwvpXyJryfjZbXcJkbSH0KJ/Zd42kd8VARY3K3Z7/AI3+qeR8TTD37+YCP/Zfh6lapdbJMcNSjaR3yR/1BONpHfBMI+LJBvkPoR+Kcs4wdza30cQrrH0a8y3O+dknheCau+0vlsWuDezGrX6WP1+SjX4RUgmzwRyu3+qXZxiObD6OH4hLs4tjO4ePRp/FU4r8ZVx8SPOGVf3m/D+q7JTVmW3c+alW8Twn3iPNrkcY7Cf9o31NvqhprxCqD6lb+wVXRnz/ACQVm/WrP7xn+Zv5rimqXiyuygZuI0o1i4XLmdYNxmwqAjNckAUo0KixyychO4ap3VRzAlQ6ypsJEkaw9UrHiHVRjXIOcqTaLJqHLIdlKR8NdoLgJhgFPc3Vwp63shqt/D4nkVyMufMsey5lCxbBJITo0kbaAkqE+0WcL6WOosb6bhabimItkBGxWcY3BleSBYdFWfh1HdA4eIcvc0S7ZLa/Pl/RL1OMZdOdgo6KXRp12GvRI4oXRvaSG95geL2PdzOA8tly8eBTnTPRcZxDWLUvH+TuJ1znANcBY2dve45bIzcR7N0bu67LfMAwttcbaga+nLcpn+sQfajYeh5jyU/BiMc8DWzNiiZG6wldmvt7Ia1pLvwXQjwuN3GL+VflHClxGS9QkzHA43tlU9htY19u8mtDS0MkUjXPa5/+ytdp8wdwoKopTDIGxuc8/cI73ncJWX/TWl3NzTi4/fvovlZg4kikHaOD3NIjt7DXHm7mfTrflYw2H/o9a5sd6kRylzhLduaDLfuZXXBv1uLeKgP7SyNOVznaaW00t4qdwSqq6iN08MZdEx7Y5JS+JoY9xAAIc4E+0NgVkxwzwWiKv+TVkycNN6pSr57EDx9g76OtdTPlZJkYzI6O4DWEXDSCTY3JJ1535qthSXEdU6WrnkeTd0jva3DQbNB8mgD0UWtso0zlp2KBqAal4oySGjckADxOgUvQ8OyzSSRQftHRi8lrAD1J15pscTe4MskYq5bEGGI2RPhSEtkcCD2ZAeNjqbC3XVN0bxVz6lKd8hEjrp9UQuHS/mjvF0iWpLYwNn8Ah2ngPguNYSQBudB5qQkwGqaLmnmA6ljra7a2Uipy5KwW4rmR+fwC7mHT6pd2HTDeKT/I/wDJJOpnjdjh5tco4zXNehLXiF7Tz+JXe18T8kQttuERDqaLoW7TxPyQSdkEWuRKRb8f4aLSXNCq74i02IXoSvwtsjdlnPFHC5F3NCUt0NaRQQEq0ossJacrhqghZBZpQKSa5GzKqLDXRmHVJgpViosu3DbmNaLpxjGJMGxVPiqntHdTKeSUm5uVv9oejTEyPAteqRZ6eozFDGMJ7Rl27qtQ1MjeRUtSY28CzmmymK/8+peXl3EQs872HI7S2lrb2SFTUOldmkdc2DRsAGjYBS+JObKL8+RUKG235JGXGoPujo5pZV3g0VOXOaxoJc42aBvqpLF2huSONp7OO7DLYlk0+8hDrWIBGUDmAT7xRKQ9nGZdnvvHCT7rfef4Wvv1IPJN5szW5M+YA3a1jnFgJ3IHX80i2FQJJGvlD3sDWn2mQWjG3u3BAPP8kQV0jTla94aCcoJuQD4/kpDDpMkErpIg9rg6Nhe02ZIW6WJG9ze2+ijKrQMb0FyfPQfID4q8M9MqjtW3PwBlBUdo23lbfzN1O8N1Mhngp2OdkdOJDE0nIX2tmIG9goOj0zO6C3qUIqgsdmDnNNjYtNjryvyT8cqyavgDKNwosOJ1TIMSqHljXtD3Ns46A2Go+BUFXsBcZG2Ac4nJa2S+oCal+h8x9NUqZAQo9Lm5dWN7fI8Kw33Yu0qWzfv5+v0o1NKWOa8btIcL7XCf0mMSRukdC98Zkv2gjcLOvfqD1Kb4di0lMXOjDDmFnZ2h2gPK+yUxHiB8zMj44RqDmYwNdpfmtSyRjCm9/Cvlz+Bjlj1PdKvj9PiF+0gROia22Zwe9xN3Oy7Dy1umjik4HI0h0QObkrDUUuQUlEK6SikpMgwN3HmFbp+IsSfEInzTmMNbIxjmAXaCGtLTlu4d4c1UWbhazR/pL7aal7eKONkMbYe7qDctLn2NrWEYs2/M6odUl+nmEop/q5GdOxGdu8kg8y4fVEOMz/3zvitmxPj7Dcsjc4zgOtkgl7zy2wAcHlvTwWfyY9Ef99qv/spqWT8lHxGZOlfm9vR+haw43z/hfVorJxqa1u05k30vrbf4fMppWVD3u/aHUabAW18FaaqZjoJZM/bgtMbf9CpYi2RxAa7tWkkWJHmq5jkjXVM7o/ZMj8n8OY2V9tll3Z349fqkC8WOO8a9Po2MUEEFYJ6Zp5EWtoWyNOibQvT+CRZos0yRl3F/C9ruaFnssZaSCNQvSVfRCRp0WUcZcNFpL2BNavcXZQg1CyXtZFslBCIRw5KdmiltlZBaKptunsVU1ReW66ymJRxlQLVk7HOw9FJ0kcTtDZVhlE7qU/pYXjmnQy+IuUCelwBrh3fkq/NgErp2QtHtmxdsAOZJ5C3NWfCal7bXU3UMDon5B3nNyk8w07gee3lfqtUscckNuYhTlCW/IovGlJGwU74HXaGGG2lzlJIfblmzO+AVWEh6p/jVPIyQh9yPdJ2UYsDhpenwNOrVuOPtDrWv42O1xsbIj5C43Py8NAkktCy5VKluTd7C50YB11KavS88mqI+neN2u+BUWyLfuCtiKUY2yRII3uEA49UaaQI4ck8iLmK5nKttMg6p4i5wa0XLiGtA5k7K2nhqjiAbV1wbJ70cTQ7IehOqgeH5Cwy1HOKM5D/7ryGMPoXX9EappRHTwyuJMk+eQE6hsTXuZqDu4uaTfotEJQhFNq2/H8+IqSlJ86RM/qXCj/v0v+Qf9q4eHsMO2IOHmwKqGQ66jTwCJ9pPh8ArfEQ/YvJ/crsn+5+ZdcNwOhimjlbiEL8jg7s5owWPHNrhmGhVrqDh8jriPDyMtsoBAzX1cLOWQCq8B8F37QOg/wD1+akeKjHlFev3I8N85P0+xrEGDUOSzqWmldckPbNLHppYZWMI6/FMsV4cpCwdjRtjfm1LqqZzCzXQXjbr7OvgVmomb90el/xTmDEi32XzN/gkLfoqlxSf+Cfzf9/wWsFcpP8APIuf9nqG5Dm1QHIQzUriD3fvvF/ePLkqxivDsglf9nimMV+4XmN0hHUhpR4uIZRtV1Q8HPfIPgXWSxx+U7ztd4y0tKfnlcUt58cucK+DX/AJYZrdS9P/AGIX9VVH/p5/+E/8kFOf2gl+/S/8Ej6MC6h7XB+2fnH7F9ll/cvJ/wDI1ynkT+JyhKeVSkEiyQNciVgkTTGMObIw6Lsbk9ifdPixEkYXxhgRheXtGnNVdrl6B4kwZsrDpyWIcQYQ6nkIt3SdPBScOqJGXQZtejJoXLolsk6Q7HQFktHUAKOM6KHoqKsmm1nRKsrSOSiqd45qVpy0ookY+pcUsrZgFW126qUdOwqVw9hYbtK24HvuZs622LfifDUU7DoCso4l4bfTPNgSzr0WsYLXnQFSWKYWyeM3A2WnJCM1UvkzJCTg7XkedmhLXsFKcS4d9nnc22h1HgoQlcvJBxk4vob4yTSa6jzDoszwTsNT4nkFY45QVWaSSyfR1CphxZO5GncD4JN1BG7djfgm0FXdOGzpbY7mJnBoj7vwJRH4DHyLh6p22ZcmqcrSeguhbJS8CIqIxFA5gJOeYb7lsbL/AFePgn3E2jKFvSkjP+fvn+ZRWIykiMH7rnnze8/g1qk3llVFD+2ijlhYISyUljZI2+w5ryMt7aWNlsScnS6L7f2Zm1Hz+5E4gQAxotpEwkgbuf33E9T3reij1OPwGdw7vZP21ZNTvuALDZ903fw/VDenl/wse76AqPBl/a/IHtIeK80RfmnAdF92Qf42n/pCNJQSt9qKRv8AE1w+oTYtP/lktxlHmq+KCTT5C9V2eb9kX5eQkDQ4DzadfkmqPlPRcQFhovaCmKPDZJmudG0ENNiS4Dz3KiYB3lNYbjLoYXwiMHMXHPnsRmFtkMr6Gzgo8O8lcQ2o0+V8+nJP+CMa64uursbLABcUpGZXW5scEqk6eVV6GVSEEyCI6RYYZU8ieoOCdP4Jk5CpIlwQ4WKp/GPDzZWO0VljkThwDhYpsRLPNGJ0LoZCxw8j1Ca5VsHHHDIe0uaNdwVlU0WRxa4WI3S5rS9uQce8hoGJQRJQOC72wS2w0kJ5SjseRzXDKEM6hB3DVuHNTNBjNt1WHSlcBJTITlFgSSZp+GYw241V4wipD27rAYJntO5V94Tx1wsCV0MWVZNnzMOXG4d5B/0pYQSO1aNtTbpzWWr0NXxtqISDbZYvjmAvjlcGC7dSLckHE4nKprnyZfD5Eri/kQbClmvSVrGxQusDRtTodxyp5HUKLDkYSIHGw0yYbUJOpnvpyAzn02Hx+ijRMlY3Xaf3iG+l7Kox3LctgtY7v2+6Gt9WtAPzukQUaWS7nHq4n4lKupJA3MY3WGpOXYdT09U9JsVY3MXQrrGuabtNj1BIKPG3MQ0NuSQABuSdAE6qaJsb3RvkGZpyuDczmhw3AI3VUi9wjMSqW+zPMP4ZJB9Clhj1WN5pHf8AyWf/ADApt2LeUrf+Z/2Ixpjyew/4ox9SExTmuTfmwdCfNegscak99sLv44Kc/PLdB2Lg+1TUp8mOb/I4JP7HLybm/g738t0jLE5vtMI/iBH1Cnb5F/k/m7/krso+HoPGYjB71I3/AASzt+pKP9qpnD/UzN/hma7+ZijSP3fouZvA/BA8jfReS+wail/9ZJ/aKf8AuJT4mYC/wYuqKzj/AMugh1y8F/4x+xdLx9X9zUYpE8ilQQSUOHsEykYJkEExAMkIZk8ilQQTUKYepiD2kFZFx7w9lcZG28fJdQTOaaFJ7lEDV0xIILJZoCiJccEEFaIBqVY+yCCIg4EgKkcMq8rgggn420xORWi5UWOHLa5Tl9RG5pLhr5IILqY5OXM5mWKjyM64kpwJC9u3NQiCC5fEr/cZ0MD7iO3QuggkDgXTmB3s+BzfAE/gggoRBKZwBuTaw3105cvNSEDnRTR9mLuDrtzBved913Vp0BB3BIQQUb2Iv1JC8LWDEHBgtGyaR7G6m0cRc9rdfBoCZ/b5ex7LOch3acpAubm1xca66FBBB18gmtvME8kpYGOLS0d0d2O4DdLB1rpGZzgxrSxoylwzANzuLj7x52tp0XUEykByEnSizRlsR7RuTm9Dt6KSpqtocwRmUXe0Fj3NdGWE2INgL/BBBV1LGEDC7QdNb8rc04+wOMbpWOa9rRd+XMCwE2Fw4C+pG111BDLZIYt2xldBBBQo/9k='
            },
            {
                'id':2, 
                'user_id': 101,
                'photo': '/9j/4AAQSkZJRgABAQEBLAEsAAD/4QBMRXhpZgAASUkqAAgAAAABAA4BAgAqAAAAGgAAAAAAAABDb250cmFzdCBvZiBzaGFkb3cgc2l6ZSBvZiB0d28gYnVzaW5lc3NtZW7/4QU8aHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIj4KCTxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CgkJPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczpJcHRjNHhtcENvcmU9Imh0dHA6Ly9pcHRjLm9yZy9zdGQvSXB0YzR4bXBDb3JlLzEuMC94bWxucy8iICAgeG1sbnM6R2V0dHlJbWFnZXNHSUZUPSJodHRwOi8veG1wLmdldHR5aW1hZ2VzLmNvbS9naWZ0LzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGx1cz0iaHR0cDovL25zLnVzZXBsdXMub3JnL2xkZi94bXAvMS4wLyIgIHhtbG5zOmlwdGNFeHQ9Imh0dHA6Ly9pcHRjLm9yZy9zdGQvSXB0YzR4bXBFeHQvMjAwOC0wMi0yOS8iIHhtbG5zOnhtcFJpZ2h0cz0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3JpZ2h0cy8iIHBob3Rvc2hvcDpDcmVkaXQ9IkdldHR5IEltYWdlcyIgR2V0dHlJbWFnZXNHSUZUOkFzc2V0SUQ9IjExNjIwODgyNTQiIHhtcFJpZ2h0czpXZWJTdGF0ZW1lbnQ9Imh0dHBzOi8vd3d3LmlzdG9ja3Bob3RvLmNvbS9sZWdhbC9saWNlbnNlLWFncmVlbWVudD91dG1fbWVkaXVtPW9yZ2FuaWMmYW1wO3V0bV9zb3VyY2U9Z29vZ2xlJmFtcDt1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'
            },
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_photo")
    op.drop_table("user_resi_history")
    op.drop_table("status_resi")
    op.drop_table("user_resi")
    op.drop_index(op.f("ix_resi_tracking_name"), table_name="resi")
    op.drop_table("resi")
    op.execute(u"DELETE FROM public.user where id in (100,101)")
    # ### end Alembic commands ###
